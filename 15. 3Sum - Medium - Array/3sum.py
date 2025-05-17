from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique efficiently
        triplets = []

        for fixed_index in range(len(nums)):
            # Skip duplicate fixed elements to avoid duplicate triplets
            if fixed_index > 0 and nums[fixed_index] == nums[fixed_index - 1]:
                continue

            left_pointer = fixed_index + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                current_sum = nums[fixed_index] + nums[left_pointer] + nums[right_pointer]

                if current_sum < 0:
                    # Sum too small, move left pointer right to increase sum
                    left_pointer += 1
                elif current_sum > 0:
                    # Sum too large, move right pointer left to decrease sum
                    right_pointer -= 1
                else:
                    # Found a triplet that sums to zero
                    triplets.append([nums[fixed_index], nums[left_pointer], nums[right_pointer]])

                    # Skip duplicates on the left pointer
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1

                    # Skip duplicates on the right pointer
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                        right_pointer -= 1

                    # Move both pointers inward for next potential pair
                    left_pointer += 1
                    right_pointer -= 1

        return triplets
