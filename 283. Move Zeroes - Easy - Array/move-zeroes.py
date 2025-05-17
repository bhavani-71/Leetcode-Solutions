class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modifies the input list in-place to move all zeroes to the end,
        preserving the relative order of non-zero elements.
        """
        insert_position = 0  # Tracks position to place the next non-zero number

        # Traverse the list
        for current_index in range(len(nums)):
            if nums[current_index] != 0:
                # Swap the current non-zero element with the element at insert_position
                nums[insert_position], nums[current_index] = nums[current_index], nums[insert_position]
                insert_position += 1
