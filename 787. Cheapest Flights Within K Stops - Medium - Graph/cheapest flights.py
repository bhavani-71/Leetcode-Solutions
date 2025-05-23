from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        # Build adjacency list: node -> list of (neighbor, price)
        for u, v, price in flights:
            graph[u].append((v, price))

        dist = [float('inf')] * n  # Distance array: min cost to reach each node
        dist[src] = 0              # Cost to reach src is 0
        q = [(src, 0)]             # Queue for BFS: (current node, cost so far)
        stops = 0                  # Number of edges used so far

        while stops <= k:
            size = len(q)
            temp = dist.copy()     # Temporary dist array to update after this level
            for _ in range(size):
                node, cost_so_far = q.pop(0)
                for neighbor, price in graph[node]:
                    new_cost = cost_so_far + price
                    # If cheaper cost found to neighbor within current stops limit
                    if new_cost < temp[neighbor]:
                        temp[neighbor] = new_cost
                        q.append((neighbor, new_cost))
            dist = temp
            stops += 1

        return dist[dst] if dist[dst] != float('inf') else -1
