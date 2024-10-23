#test_cases.py

import unittest
from rule_engine import create_rule, combine_rules, evaluate_rule
from ast_node import ASTNode

class TestRuleEngine(unittest.TestCase):
    
    def test_create_rule(self):
        rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        self.assertIsInstance(ast, ASTNode)
        self.assertEqual(ast.value, 'AND')
    
    def test_combine_rules(self):
        rule1 = create_rule("age > 30 AND department = 'Sales'")
        rule2 = create_rule("salary > 50000")
        combined_ast = combine_rules([rule1, rule2], "AND")
        self.assertIsNotNone(combined_ast)
        self.assertEqual(combined_ast.value, 'AND')

    def test_evaluate_rule(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule_string)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()