# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Returns True if the binary tree rooted at 'root' is a valid Binary Search Tree.
        """

        def validate_bst(node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
            # Base case: An empty node is always valid
            if not node:
                return True

            # The current node's value must be within the valid range
            if not (lower_bound < node.val < upper_bound):
                return False

            # Recursively validate the right subtree with updated lower bound
            is_right_valid = validate_bst(node.right, node.val, upper_bound)

            # Recursively validate the left subtree with updated upper bound
            is_left_valid = validate_bst(node.left, lower_bound, node.val)

            return is_left_valid and is_right_valid

        # Start with the entire range of valid values
        return validate_bst(root, float('-inf'), float('inf'))
