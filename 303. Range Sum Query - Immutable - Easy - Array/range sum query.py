from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Initialize prefix_sum array where each index stores sum from 0 to that index
        self.prefix_sum = [0] * len(nums)
        self.prefix_sum[0] = nums[0]
        
        for i in range(1, len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # If starting index is 0, return the prefix sum up to 'right'
        if left == 0:
            return self.prefix_sum[right]
        # Otherwise, return the difference of prefix sums
        return self.prefix_sum[right] - self.prefix_sum[left - 1]

# Example Usage:
# obj = NumArray([1, 2, 3, 4])
# print(obj.sumRange(1, 3))  # Output: 9 (2+3+4)
