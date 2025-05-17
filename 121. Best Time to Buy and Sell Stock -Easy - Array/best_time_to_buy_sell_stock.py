from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize max profit to zero (no transaction made yet)
        max_profit = 0
        
        # Initialize minimum price to the first day's price
        min_price = prices[0]

        # Iterate over prices starting from the second day
        for price in prices[1:]:
            # Update minimum price if current price is lower
            min_price = min(min_price, price)
            
            # Calculate current profit if selling at current price
            current_profit = price - min_price
            
            # Update max profit if current profit is higher
            max_profit = max(max_profit, current_profit)
        
        # Return the maximum profit found
        return max_profit
