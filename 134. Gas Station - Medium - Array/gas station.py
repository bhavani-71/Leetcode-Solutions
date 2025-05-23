from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0  # Total gas surplus over the entire trip
        current_tank = 0   # Gas in tank at the current station
        start_index = 0    # Index from which we attempt to start

        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            total_surplus += net_gain
            current_tank += net_gain

            # If at any point tank goes negative, can't start from this segment
            if current_tank < 0:
                start_index = i + 1  # Try next station as new start
                current_tank = 0     # Reset tank
                # print(gas[i])  # For debugging only

        # If total gas is enough to cover total cost, return starting index
        return start_index if total_surplus >= 0 else -1
