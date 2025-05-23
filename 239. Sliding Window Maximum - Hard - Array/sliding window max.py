from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window_indices = deque()  # stores indices of elements in decreasing order of their values
        max_values = []

        for current_index in range(len(nums)):
            # Remove indices that are out of the current window bounds
            if window_indices and window_indices[0] <= current_index - k:
                window_indices.popleft()

            # Remove elements smaller than the current element from the back
            while window_indices and nums[window_indices[-1]] < nums[current_index]:
                window_indices.pop()

            # Add current element's index to the deque
            window_indices.append(current_index)

            # Start adding max values once the first full window is formed
            if current_index >= k - 1:
                max_values.append(nums[window_indices[0]])

        return max_values
