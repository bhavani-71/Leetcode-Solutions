from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list representing graph: course -> list of next courses
        adjacency = defaultdict(list)
        for course, prereq in prerequisites:
            adjacency[prereq].append(course)

        # State definitions for DFS traversal
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # Track visitation state of each course
        states = [UNVISITED] * numCourses
        order = []  # Stores the topological order of courses

        def dfs(course: int) -> bool:
            # If course is already fully processed, no cycle here
            if states[course] == VISITED:
                return True
            
            # If course is being visited in current recursion stack, cycle detected
            if states[course] == VISITING:
                return False
            
            # Mark course as visiting
            states[course] = VISITING
            
            # Visit all courses dependent on current course
            for next_course in adjacency[course]:
                if not dfs(next_course):
                    return False  # Cycle detected in recursion
            
            # Mark course as visited after processing neighbors
            states[course] = VISITED
            order.append(course)  # Add to order after dependencies
            
            return True

        # Perform DFS for each course
        for c in range(numCourses):
            if states[c] == UNVISITED:
                if not dfs(c):  # If cycle detected, return empty list
                    return []

        # Reverse to get correct order since we append after visiting dependencies
        return order[::-1]
