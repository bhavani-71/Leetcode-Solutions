class Solution:
    def climbStairs(self, total_steps: int) -> int:
        # If the staircase has 1 or 2 steps, return the number of steps directly
        if total_steps <= 2:
            return total_steps

        # Initialize ways to reach step 1 and step 2
        ways_to_reach_step_1 = 1
        ways_to_reach_step_2 = 2

        # Calculate ways for steps from 3 to total_steps
        for current_step in range(3, total_steps + 1):
            # Number of ways to reach current step = 
            # ways to reach previous step + ways to reach step before previous
            current_ways = ways_to_reach_step_1 + ways_to_reach_step_2
            # Update variables for next iteration
            ways_to_reach_step_1 = ways_to_reach_step_2
            ways_to_reach_step_2 = current_ways

        return ways_to_reach_step_2
