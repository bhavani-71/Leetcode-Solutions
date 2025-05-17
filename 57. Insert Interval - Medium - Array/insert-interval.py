from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        total_intervals = len(intervals)
        merged_intervals = []
        index = 0
        
        # Add all intervals ending before new_interval starts (no overlap)
        while index < total_intervals and intervals[index][1] < new_interval[0]:
            merged_intervals.append(intervals[index])
            index += 1
        
        # Merge overlapping intervals with new_interval
        while index < total_intervals and intervals[index][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[index][0])
            new_interval[1] = max(new_interval[1], intervals[index][1])
            index += 1
        
        # Add merged new_interval
        merged_intervals.append(new_interval)
        
        # Add remaining intervals after new_interval
        while index < total_intervals:
            merged_intervals.append(intervals[index])
            index += 1
        
        return merged_intervals
