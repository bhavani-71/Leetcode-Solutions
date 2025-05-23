class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        def can_finish(speed: int) -> bool:
            total_hours = 0
            for pile in piles:
                # Hours needed to eat each pile at current speed
                total_hours += ceil(pile / speed)
            # Check if total hours is within allowed time h
            return total_hours <= h

        left = 1  # Minimum possible eating speed
        right = max(piles)  # Maximum possible eating speed (eat the largest pile in one hour)

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                # If can finish eating at speed mid, try to find smaller speed
                right = mid
            else:
                # If cannot finish, need to increase speed
                left = mid + 1

        return right
