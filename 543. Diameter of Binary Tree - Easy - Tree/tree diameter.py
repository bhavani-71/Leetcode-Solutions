# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        self.max_diameter = 0  # Stores the maximum diameter found so far

        def depth(node: Optional['TreeNode']) -> int:
            # Base case: if node is None, return 0 depth
            if not node:
                return 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Possible diameter at this node is sum of left and right depths
            current_diameter = left_depth + right_depth
            
            # Update max_diameter if current diameter is larger
            if current_diameter > self.max_diameter:
                self.max_diameter = current_diameter
            
            # Return depth of current node = 1 + max depth of its subtrees
            return 1 + max(left_depth, right_depth)
        
        # Start DFS traversal from root
        depth(root)
        
        return self.max_diameter
