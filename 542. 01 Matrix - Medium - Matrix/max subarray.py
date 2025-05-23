from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Given a binary matrix 'mat', return a matrix where each cell contains
        the distance to the nearest 0 in 'mat'.
        """

        # Dimensions of the matrix
        rows, cols = len(mat), len(mat[0])

        # Result matrix initialized with -1 indicating unvisited cells
        distance_matrix = [[-1 for _ in range(cols)] for _ in range(rows)]

        # Queue for BFS (stores tuples of cell coordinates)
        bfs_queue = deque()

        # Initialize BFS queue with all cells that contain 0, and set their distance to 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    distance_matrix[r][c] = 0
                    bfs_queue.append((r, c))

        # Directions for exploring adjacent cells (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Process BFS until all reachable cells are visited
        while bfs_queue:
            current_row, current_col = bfs_queue.popleft()

            # Check all 4 neighbors of the current cell
            for dr, dc in directions:
                neighbor_row, neighbor_col = current_row + dr, current_col + dc

                # If neighbor is inside matrix bounds and unvisited (-1)
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and distance_matrix[neighbor_row][neighbor_col] == -1:
                    # Update neighbor's distance as current cell's distance + 1
                    distance_matrix[neighbor_row][neighbor_col] = distance_matrix[current_row][current_col] + 1
                    # Add neighbor to the queue to continue BFS from there
                    bfs_queue.append((neighbor_row, neighbor_col))

        return distance_matrix
