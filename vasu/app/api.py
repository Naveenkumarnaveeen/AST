#api.py

from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

# In-memory storage for ASTs
rule_asts = {}

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    rule_id = data.get('rule_id')
    rule_ast = create_rule(rule_string)
    rule_asts[rule_id] = rule_ast
    return jsonify({'message': 'Rule created successfully', 'rule_id': rule_id})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rule_ids = data.get('rule_ids')
    operator = data.get('operator', 'AND')
    rules_to_combine = [rule_asts[rule_id] for rule_id in rule_ids]
    combined_ast = combine_rules(rules_to_combine, operator)
    return jsonify({'message': 'Rules combined successfully'})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    rule_id = data.get('rule_id')
    attributes = data.get('attributes')
    rule_ast = rule_asts.get(rule_id)
    result = evaluate_rule(rule_ast, attributes)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)