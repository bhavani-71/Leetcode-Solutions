import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def squared_distance(x: int, y: int) -> int:
            # Calculate squared Euclidean distance from origin
            return x*x + y*y
        
        max_heap = []  # max heap to store k closest points, store (-distance, x, y)
        
        for x, y in points:
            dist = squared_distance(x, y)
            
            # If heap size less than k, push current point
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, x, y))
            else:
                # If current point is closer than the farthest in heap, replace it
                heapq.heappushpop(max_heap, (-dist, x, y))
        
        # Extract points from heap (discard distances)
        return [(x, y) for _, x, y in max_heap]