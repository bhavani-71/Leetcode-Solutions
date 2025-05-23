# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Dictionary to map original node to its clone
        cloned_nodes = {}

        def dfs(current_node):
            # If already cloned, return it
            if current_node in cloned_nodes:
                return cloned_nodes[current_node]

            # Clone the current node
            copy = Node(current_node.val)
            cloned_nodes[current_node] = copy

            # Recursively clone all neighbors
            for neighbor in current_node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
