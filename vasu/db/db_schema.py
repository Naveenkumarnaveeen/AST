#db_schema.py

{
  "_id": "rule1",
  "name": "Age and Department Rule",
  "AST": {
    "type": "operator",
    "value": "AND",
    "left": {
      "type": "operator",
      "value": "OR",
      "left": {
        "type": "operator",
        "value": "AND",
        "left": { "type": "operand", "value": "age > 30" },
        "right": { "type": "operand", "value": "department = 'Sales'" }
      },
      "right": {
        "type": "operator",
        "value": "AND",
        "left": { "type": "operand", "value": "age < 25" },
        "right": { "type": "operand", "value": "department = 'Marketing'" }
      }
    },
    "right": {
      "type": "operator",
      "value": "OR",
      "left": { "type": "operand", "value": "salary > 50000" },
      "right": { "type": "operand", "value": "experience > 5" }
    }
  }
}