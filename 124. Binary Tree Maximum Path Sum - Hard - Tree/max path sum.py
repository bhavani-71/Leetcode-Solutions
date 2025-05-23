# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')  # Global max path sum
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._dfs(root)
        return self.max_sum
    
    def _dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        # Recursively find max gain from left subtree; ignore negative gains
        left_gain = max(self._dfs(node.left), 0)
        # Recursively find max gain from right subtree; ignore negative gains
        right_gain = max(self._dfs(node.right), 0)
        
        # Calculate current path sum passing through this node
        current_path_sum = node.val + left_gain + right_gain
        
        # Update global max_sum if current_path_sum is greater
        self.max_sum = max(self.max_sum, current_path_sum)
        
        # Return max gain including this node and one subtree for parent's path calculation
        return node.val + max(left_gain, right_gain)