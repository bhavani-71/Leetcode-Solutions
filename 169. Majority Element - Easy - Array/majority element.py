class Solution:
    def majorityElement(self, numbers: List[int]) -> int:
        count = 0
        majority_candidate = None

        # Boyer-Moore Voting Algorithm
        for number in numbers:
            if count == 0:
                majority_candidate = number
            count += 1 if number == majority_candidate else -1

        return majority_candidate
