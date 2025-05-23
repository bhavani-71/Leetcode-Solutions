from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list representation of the graph
        course_graph = defaultdict(list)
        for course, prereq in prerequisites:
            course_graph[course].append(prereq)

        # State definitions
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        # Track the state of each course
        course_state = [UNVISITED] * numCourses

        def hasCycle(course: int) -> bool:
            """Return False if a cycle is detected, True otherwise"""
            if course_state[course] == VISITED:
                return True  # Already checked, no cycle through this node
            if course_state[course] == VISITING:
                return False  # Cycle detected

            # Mark as visiting
            course_state[course] = VISITING

            # Recursively visit all prerequisites
            for prereq in course_graph[course]:
                if not hasCycle(prereq):
                    return False

            # Mark as visited after all neighbors are processed
            course_state[course] = VISITED
            return True

        # Check each course for cycles
        for course in range(numCourses):
            if not hasCycle(course):
                return False  # If a cycle is found, courses can't be finished

        return True  # All courses can be finished if no cycles are found
