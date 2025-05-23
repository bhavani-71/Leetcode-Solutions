from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0           # Result: max length of valid substring
        left = 0                 # Left pointer for sliding window
        max_freq = 0             # Max frequency of a single character in current window
        char_freq = defaultdict(int)  # Frequency dictionary for chars in current window
        
        for right in range(len(s)):
            current_char = s[right]
            char_freq[current_char] += 1

            # Update max frequency in the current window
            max_freq = max(max_freq, char_freq[current_char])

            # If window size minus max_freq > k, shrink window from left
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                char_freq[left_char] -= 1
                left += 1  # shrink the window from the left
            
            # Update max_length for the largest valid window so far
            current_window_length = right - left + 1
            max_length = max(max_length, current_window_length)
        
        return max_length
