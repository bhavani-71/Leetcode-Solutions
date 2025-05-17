class Solution:
    def containsDuplicate(self, numbers: List[int]) -> bool:
        seen_numbers = set()  # Set to store unique elements

        for number in numbers:
            if number in seen_numbers:
                # Duplicate found
                return True
            seen_numbers.add(number)  # Add number to the set

        # No duplicates found
        return False
