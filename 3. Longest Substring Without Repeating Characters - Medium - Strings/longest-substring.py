class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        charIndex = {}
        # Start index of current substring without duplicates
        start = 0
        # Maximum length found so far
        maxLength = 0
        
        for i in range(len(s)):
            # If character is already seen and inside the current window
            if s[i] in charIndex and charIndex[s[i]] >= start:
                # Move start to one position right of the last occurrence
                start = charIndex[s[i]] + 1
            
            # Update last seen index of current character
            charIndex[s[i]] = i
            
            # Calculate current window length and update maxLength
            maxLength = max(maxLength, i - start + 1)
        
        return maxLength
