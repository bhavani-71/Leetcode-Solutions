class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor_sum = 0
       
        # Compute total XOR
        for num in nums:
            xor_sum ^= num


        # If XOR is already 0, first player wins immediately
        if xor_sum == 0:
            return True


        # If number of elements is even, first player can force a win
        return len(nums) % 2 == 0
