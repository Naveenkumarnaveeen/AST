#rule_engine.py

import ast
from ast_node import ASTNode

# Function to create a rule AST from a rule string
def create_rule(rule_string):
    def parse_to_ast(node):
        if isinstance(node, ast.BoolOp):
            operator = 'AND' if isinstance(node.op, ast.And) else 'OR'
            return ASTNode('operator', parse_to_ast(node.values[0]), parse_to_ast(node.values[1]), operator)
        elif isinstance(node, ast.Compare):
            left = node.left.id
            comparator = node.ops[0]
            if isinstance(comparator, ast.Gt):
                comp_op = '>'
            elif isinstance(comparator, ast.Lt):
                comp_op = '<'
            right = node.comparators[0].n
            return ASTNode('operand', value=f'{left} {comp_op} {right}')
    
    tree = ast.parse(rule_string, mode='eval')
    root = parse_to_ast(tree.body)
    return root

# Function to combine multiple ASTs into one using a specified operator (AND/OR)
def combine_rules(rule_asts, operator="AND"):
    if len(rule_asts) == 0:
        return None
    root = rule_asts[0]
    for rule in rule_asts[1:]:
        root = ASTNode('operator', left=root, right=rule, value=operator)
    return root

# Function to evaluate the rule AST against user data
def evaluate_rule(ast_node, data):
    if ast_node.type == 'operand':
        key, op, value = ast_node.value.split()
        value = int(value)  # Convert to integer for comparisons
        if op == '>':
            return data[key] > value
        elif op == '<':
            return data[key] < value
        elif op == '=':
            return data[key] == value
    elif ast_node.type == 'operator':
        left_eval = evaluate_rule(ast_node.left, data)
        right_eval = evaluate_rule(ast_node.right, data)
        if ast_node.value == 'AND':
            return left_eval and right_eval
        elif ast_node.value == 'OR':
            return left_eval or right_eval