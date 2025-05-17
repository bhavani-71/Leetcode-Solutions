# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the current node is None, return None
        if not root:
            return None
        
        # Recursively invert the right subtree and assign to left child
        root.left = self.invertTree(root.right)
        # Recursively invert the left subtree and assign to right child
        root.right = self.invertTree(root.left)
        
        # Return the root node after inverting subtrees
        return root
