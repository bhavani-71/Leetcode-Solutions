from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency map for chars in t
        target_counts = Counter(t)
        window_counts = {}

        have, need = 0, len(target_counts)
        left = 0
        result_range = [-1, -1]
        result_length = float("inf")

        # Expand window with right pointer
        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0) + 1

            # If current char frequency matches required count in t, increment have
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # Try shrinking window when all chars matched
            while have == need:
                window_size = right - left + 1
                if window_size < result_length:
                    result_length = window_size
                    result_range = [left, right]

                # Shrink from left
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                left += 1

        left, right = result_range
        return s[left:right+1] if result_length != float("inf") else ""
