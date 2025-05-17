class Solution:
    def search(self, sorted_list: List[int], target_value: int) -> int:
        """
        Performs binary search on a sorted list to find the target value.
        Returns the index of the target if found, otherwise returns -1.
        """
        left_pointer, right_pointer = 0, len(sorted_list) - 1

        while left_pointer <= right_pointer:
            middle_index = (left_pointer + right_pointer) // 2

            # Check if the middle element is the target
            if sorted_list[middle_index] == target_value:
                return middle_index
            elif sorted_list[middle_index] < target_value:
                # Target lies in the right half
                left_pointer = middle_index + 1
            else:
                # Target lies in the left half
                right_pointer = middle_index - 1

        # Target not found
        return -1
