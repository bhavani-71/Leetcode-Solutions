import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        
        # Min-heap to store the next minimum cost edge (cost, point_index)
        min_heap = [(0, 0)]
        
        # Set to keep track of visited points
        visited_nodes = set()
        
        # Total minimum cost to connect all points
        total_connection_cost = 0

        # While there are still points to connect
        while len(visited_nodes) < num_points:
            cost_to_connect, current_point = heapq.heappop(min_heap)

            # If already visited, skip
            if current_point in visited_nodes:
                continue

            # Mark this point as visited and add its cost
            visited_nodes.add(current_point)
            total_connection_cost += cost_to_connect

            # Compare current point with all unvisited points
            for next_point in range(num_points):
                if next_point not in visited_nodes:
                    x1, y1 = points[current_point]
                    x2, y2 = points[next_point]
                    manhattan_distance = abs(x1 - x2) + abs(y1 - y2)

                    # Add edge to heap
                    heapq.heappush(min_heap, (manhattan_distance, next_point))

        return total_connection_cost