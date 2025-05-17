from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], start_row: int, start_col: int, new_color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[start_row][start_col]
        
        # If the original color is same as new color, no need to fill
        if original_color == new_color:
            return image
        
        queue = deque()
        queue.append((start_row, start_col))
        
        # Directions for neighbors: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            current_row, current_col = queue.popleft()
            
            # Fill only if the pixel has the original color
            if image[current_row][current_col] == original_color:
                image[current_row][current_col] = new_color
                
                # Check all 4 neighbors
                for dr, dc in directions:
                    neighbor_row, neighbor_col = current_row + dr, current_col + dc
                    
                    # Check boundaries before adding neighbor to queue
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        if image[neighbor_row][neighbor_col] == original_color:
                            queue.append((neighbor_row, neighbor_col))
        
        return image
