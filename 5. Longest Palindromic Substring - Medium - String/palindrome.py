class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""  # Store the longest palindrome found
        
        for center in range(len(s)):
            # Check for odd length palindrome (single center)
            palindrome_odd = self.expandAroundCenter(s, center, center)
            
            # Check for even length palindrome (center between two characters)
            palindrome_even = self.expandAroundCenter(s, center, center + 1)
            
            # Update longest palindrome if we found a longer one
            if len(palindrome_odd) > len(longest_palindrome):
                longest_palindrome = palindrome_odd
            if len(palindrome_even) > len(longest_palindrome):
                longest_palindrome = palindrome_even
        
        return longest_palindrome

    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        # Expand as long as the characters at left and right are equal and within bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindrome substring found between left+1 and right-1 indices
        return s[left + 1:right]
