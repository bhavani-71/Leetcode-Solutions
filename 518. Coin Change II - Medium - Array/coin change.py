from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] will store the number of ways to make up amount 'i'
        dp = [0] * (amount + 1)

        # Base case: There is 1 way to make amount 0 (by choosing no coins)
        dp[0] = 1

        # Iterate through each coin
        for coin in coins:
            # For each amount from coin to total amount, update the number of ways
            for current_amount in range(coin, amount + 1):
                # The current amount can be formed by:
                # (ways to form current_amount - coin) + existing ways to form current_amount
                dp[current_amount] += dp[current_amount - coin]

        # The final answer is the number of ways to form the original amount
        return dp[amount]
