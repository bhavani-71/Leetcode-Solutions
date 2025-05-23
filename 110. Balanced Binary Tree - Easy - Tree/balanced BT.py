# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.
        A binary tree is balanced if the depth of the two subtrees of every node never differ by more than 1.

        Args:
            root (TreeNode): The root of the binary tree.

        Returns:
            bool: True if the tree is balanced, False otherwise.
        """

        def check(node):
            if not node:
                return 0  # Height of empty subtree is 0
            
            # Check left subtree height
            left = check(node.left)
            if left == -1:  # Left subtree is unbalanced
                return -1
            
            # Check right subtree height
            right = check(node.right)
            if right == -1:  # Right subtree is unbalanced
                return -1
            
            # If current node's subtrees differ in height by more than 1, unbalanced
            if abs(right - left) > 1:
                return -1
            
            # Return height of current node
            return 1 + max(left, right)

        # Tree is balanced if check(root) != -1
        return check(root) != -1
