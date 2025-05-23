from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build adjacency list for the undirected graph
        adjacency = defaultdict(list)
        for u, v in connections:
            adjacency[u].append(v)
            adjacency[v].append(u)

        disc = [-1] * n  # Discovery time of each node
        low = [-1] * n   # Lowest discovery time reachable from node
        time = [0]       # Global timer wrapped in list to pass by reference
        result = []      # List to store critical connections (bridges)

        def dfs(u: int, parent: int):
            # Assign discovery time and low value
            disc[u] = low[u] = time[0]
            time[0] += 1

            # Explore all adjacent nodes
            for v in adjacency[u]:
                if v == parent:
                    continue  # Skip the parent node to avoid trivial cycle

                if disc[v] == -1:  # If v is not visited
                    dfs(v, u)
                    # Update low[u] based on child's low[v]
                    low[u] = min(low[u], low[v])

                    # Check if edge u-v is a bridge
                    if low[v] > disc[u]:
                        result.append([u, v])
                else:
                    # Update low[u] for back edge
                    low[u] = min(low[u], disc[v])

        # Call DFS for every node to cover disconnected graph components
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return result
