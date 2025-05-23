from typing import List
from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create a list to hold all the critical points (start and end of buildings)
        critical_points = []
        
        # For each building, add start point with negative height (for max heap)
        # and end point with zero height (to signify removal)
        for left, right, height in buildings:
            critical_points.append((left, -height, right))  # Start point
            critical_points.append((right, 0, 0))           # End point
        
        # Sort points by x-coordinate, and start points before end points if same x
        critical_points.sort()
        
        # Max heap to track active buildings (height, end_x)
        # Initialize with ground level (height 0, ends at infinity)
        active_buildings = [(0, float('inf'))]
        
        # Result list for skyline key points
        skyline = []
        
        for x_coord, neg_height, end_x in critical_points:
            if neg_height < 0:  # Start of building
                # Add building height and end position to heap
                heappush(active_buildings, (neg_height, end_x))
            else:  # End of building
                # Remove all buildings from heap which have ended by x_coord
                while active_buildings and active_buildings[0][1] <= x_coord:
                    heappop(active_buildings)
            
            # Current max height is the negative of the smallest height in max heap
            current_max_height = -active_buildings[0][0]
            
            # If height changed from previous point, add new key point to skyline
            if not skyline or skyline[-1][1] != current_max_height:
                skyline.append([x_coord, current_max_height])
        
        return skyline
