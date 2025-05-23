from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)  # Count frequency of each number
        bucket = [[] for _ in range(len(nums) + 1)]  # Buckets for frequencies
        
        # Place numbers in buckets corresponding to their frequencies
        for num, freq in frequency.items():
            bucket[freq].append(num)
        
        result = []
        # Iterate from highest frequency to lowest
        for freq in range(len(bucket) - 1, -1, -1):
            if bucket[freq]:
                result.extend(bucket[freq])
                if len(result) >= k:
                    return result[:k]
        return result[:k]
