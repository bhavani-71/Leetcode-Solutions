from typing import List

class Solution:
    def coinChange(self, coin_denominations: List[int], target_amount: int) -> int:
        """
        Returns the minimum number of coins required to make up the given target_amount
        using the available coin_denominations. If it's not possible, returns -1.
        """

        # Initialize a list to store minimum coins needed for each amount from 0 to target_amount.
        # Set initial values to infinity. dp[0] = 0 since 0 coins are needed to make amount 0.
        min_coins_needed = [float('inf')] * (target_amount + 1)
        min_coins_needed[0] = 0

        # Loop through each coin denomination
        for coin in coin_denominations:
            # Update dp values for amounts from coin to target_amount
            for current_amount in range(coin, target_amount + 1):
                # Either don't take this coin, or take it and add 1 to the result of (amount - coin)
                min_coins_needed[current_amount] = min(
                    min_coins_needed[current_amount],
                    min_coins_needed[current_amount - coin] + 1
                )

        # Debugging: print the dp array (optional)
        print(min_coins_needed)

        # If target amount is still infinity, it's not possible to form it with given coins
        return min_coins_needed[target_amount] if min_coins_needed[target_amount] != float('inf') else -1
