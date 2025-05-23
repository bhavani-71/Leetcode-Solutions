from fractions import Fraction
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        total_points = len(points)
        
        # If there are 2 or fewer points, all are on the same line
        if total_points <= 2:
            return total_points
        
        max_points_on_line = 0
        
        # Iterate through each point to consider it as a base
        for i in range(total_points):
            duplicates = 1  # Count of points that are identical to base point
            slope_count = defaultdict(int)  # Slope to count of points
            x1, y1 = points[i]
            
            # Compare base point with all other points
            for j in range(i + 1, total_points):
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    # Identical point to base
                    duplicates += 1
                elif x1 == x2:
                    # Vertical line (infinite slope)
                    slope = "inf"
                    slope_count[slope] += 1
                else:
                    # Calculate slope using Fraction to avoid float precision issues
                    slope = Fraction(y2 - y1, x2 - x1)
                    slope_count[slope] += 1
            
            # Max points on a line through current base point
            max_points_through_base = max(slope_count.values(), default=0)
            
            # Include duplicate points in the final count
            max_points_on_line = max(max_points_on_line, max_points_through_base + duplicates)
        
        return max_points_on_line
