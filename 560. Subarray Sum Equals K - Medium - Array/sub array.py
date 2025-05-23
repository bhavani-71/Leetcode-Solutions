from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarrays = 0
        current_prefix_sum = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1  # Base case: one subarray with sum = 0

        for num in nums:
            # Step 1: Add current number to running prefix sum
            current_prefix_sum += num
            
            # Step 2: Check if there exists a prefix_sum such that:
            # current_prefix_sum - previous_prefix_sum = k
            if (current_prefix_sum - k) in prefix_sum_counts:
                total_subarrays += prefix_sum_counts[current_prefix_sum - k]
            
            # Step 3: Record the current prefix sum
            prefix_sum_counts[current_prefix_sum] += 1
        
        return total_subarrays
