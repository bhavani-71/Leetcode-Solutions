from typing import List

class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        # Ensure arr1 is the smaller array for efficient binary search
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        m, n = len(arr1), len(arr2)
        low, high = 0, m
        
        while low <= high:
            partition_arr1 = (low + high) // 2
            partition_arr2 = (m + n + 1) // 2 - partition_arr1
            
            # Left max elements or -inf if partition is at the start
            max_left_arr1 = float("-inf") if partition_arr1 == 0 else arr1[partition_arr1 - 1]
            max_left_arr2 = float("-inf") if partition_arr2 == 0 else arr2[partition_arr2 - 1]
            
            # Right min elements or +inf if partition is at the end
            min_right_arr1 = float("inf") if partition_arr1 == m else arr1[partition_arr1]
            min_right_arr2 = float("inf") if partition_arr2 == n else arr2[partition_arr2]
            
            # Check if correct partition is found
            if max_left_arr1 <= min_right_arr2 and max_left_arr2 <= min_right_arr1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(max_left_arr1, max_left_arr2) + min(min_right_arr1, min_right_arr2)) / 2
                else:  # If total length is odd
                    return max(max_left_arr1, max_left_arr2)
            elif max_left_arr1 > min_right_arr2:
                # Move partition_arr1 to the left
                high = partition_arr1 - 1
            else:
                # Move partition_arr1 to the right
                low = partition_arr1 + 1
