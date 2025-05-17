from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequency of each character in the string
        freq = Counter(s)
        l = 0  # length of palindrome that can be formed
        odd = False  # flag to check if any character has an odd count

        for val in freq.values():
            if val % 2 == 0:
                # If frequency is even, add entire count
                l += val
            else:
                # If frequency is odd, add the largest even number smaller than val
                l += val - 1
                odd = True  # mark that we found an odd frequency

        # If any odd frequency exists, we can put one odd character in the center
        return l + 1 if odd else l
