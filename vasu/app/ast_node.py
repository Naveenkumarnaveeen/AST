#ast_node.py

class ASTNode:
    def _init_(self, node_type, left=None, right=None, value=None):
        """
        :param node_type: 'operator' for AND/OR, 'operand' for conditions.
        :param left: Left child node (can be another ASTNode or None).
        :param right: Right child node (can be another ASTNode or None).
        :param value: Condition string (like 'age > 30') or operator (AND/OR).
        """
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # Left child node
        self.right = right     # Right child node
        self.value = value     # Optional condition value for operand nodes