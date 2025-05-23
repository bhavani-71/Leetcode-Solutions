# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If current node is None, depth is 0
        if not root:
            return 0
        
        # Recursively find max depth of left subtree
        left_depth = self.maxDepth(root.left)
        
        # Recursively find max depth of right subtree
        right_depth = self.maxDepth(root.right)
        
        # Max depth at current node is 1 + max of left and right depths
        return 1 + max(left_depth, right_depth)
