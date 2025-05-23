class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the middle element is the target
            if target == nums[mid]:
                return mid
            
            # Determine which side is sorted
            if nums[left] <= nums[mid]:
                # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the left sorted portion
                    right = mid - 1
                else:
                    # Target is in the right portion
                    left = mid + 1
            else:
                # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the right sorted portion
                    left = mid + 1
                else:
                    # Target is in the left portion
                    right = mid - 1
        
        # Target not found
        return -1
