from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        # Depth-First Search to mark reachable cells
        def dfs(row, col, visited, prev_height):
            # Check for out-of-bounds or already visited or invalid flow
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                (row, col) in visited or 
                heights[row][col] < prev_height):
                return

            visited.add((row, col))

            # Explore neighbors
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        # Start DFS from Pacific and Atlantic border cells
        for col in range(cols):
            dfs(0, col, pacific_reachable, heights[0][col])        # Top border (Pacific)
            dfs(rows - 1, col, atlantic_reachable, heights[rows-1][col])  # Bottom border (Atlantic)

        for row in range(rows):
            dfs(row, 0, pacific_reachable, heights[row][0])        # Left border (Pacific)
            dfs(row, cols - 1, atlantic_reachable, heights[row][cols-1])  # Right border (Atlantic)

        # Cells reachable from both oceans
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    result.append([row, col])

        return result
