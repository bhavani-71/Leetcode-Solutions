from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr, right_ptr = 0, len(height) - 1          # Two pointers at start and end
        max_left, max_right = 0, 0                         # Track max height from left and right
        trapped_water = 0                                  # Result accumulator

        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                if height[left_ptr] >= max_left:
                    max_left = height[left_ptr]           # Update left max if current is higher
                else:
                    trapped_water += max_left - height[left_ptr]  # Water trapped at left_ptr
                    print(left_ptr, right_ptr, trapped_water)
                left_ptr += 1
            else:
                if height[right_ptr] >= max_right:
                    max_right = height[right_ptr]         # Update right max if current is higher
                else:
                    trapped_water += max_right - height[right_ptr] # Water trapped at right_ptr
                    print(left_ptr, right_ptr, trapped_water)
                right_ptr -= 1

        return trapped_water
