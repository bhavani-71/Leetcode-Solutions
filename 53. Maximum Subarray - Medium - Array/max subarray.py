from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray within an array which has the largest sum.

        Args:
            nums (List[int]): List of integers.

        Returns:
            int: The maximum sum of a contiguous subarray.
        """

        max_sum = c_sum = nums[0]  # Initialize max sum and current sum with first element
        for i in nums[1:]:
            # For each element, decide whether to start a new subarray or continue the existing one
            c_sum = max(i, c_sum + i)
            # Update max_sum if current sum is greater
            max_sum = max(max_sum, c_sum)
        return max_sum
