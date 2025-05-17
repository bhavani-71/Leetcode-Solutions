from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Dictionary to store number and its index
        hashmap = {}

        # Loop through each number in the list
        for i in range(len(numbers)):
            # Calculate the difference needed to reach the target
            remaining = target - numbers[i]

            # Check if the remaining value is already in the hashmap
            if remaining in hashmap:
                # If found, return the current index and the index of the remaining number
                return [i, hashmap[remaining]]

            # If not found, store the current number and its index in hashmap
            hashmap[numbers[i]] = i

        # If no solution is found (shouldn't happen as per problem statement)
        return []
