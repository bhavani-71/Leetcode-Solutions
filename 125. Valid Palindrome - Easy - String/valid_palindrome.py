class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers at start and end of the string
        start = 0
        end = len(s) - 1
        
        # Loop until pointers cross
        while start < end:
            # Move start forward if current char is not alphanumeric
            while start < end and not s[start].isalnum():
                start += 1
            
            # Move end backward if current char is not alphanumeric
            while start < end and not s[end].isalnum():
                end -= 1
            
            # Compare characters in lowercase
            if s[start].lower() != s[end].lower():
                return False  # Mismatch found, not a palindrome
            
            # Move both pointers inward
            start += 1
            end -= 1
        
        # If all matched, it is a palindrome
        return True
