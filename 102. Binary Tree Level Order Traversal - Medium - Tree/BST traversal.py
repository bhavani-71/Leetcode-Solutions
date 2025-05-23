# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)  # Number of nodes at current level
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()  # Dequeue node
                level_nodes.append(node.val)  # Add node's value
                
                # Enqueue children if present
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_nodes)  # Add current level to result
        
        return result
