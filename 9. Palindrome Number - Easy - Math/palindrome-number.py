class Solution:
    def isPalindrome(self, number: int) -> bool:
        # Negative numbers and numbers ending with 0 (but not 0 itself) are not palindromes
        if number < 0 or (number % 10 == 0 and number != 0):
            return False

        reversed_half = 0  # To reverse half of the number

        # Build the reversed half until it's greater than or equal to the remaining number
        while number > reversed_half:
            last_digit = number % 10
            reversed_half = reversed_half * 10 + last_digit
            number //= 10  # Remove the last digit from the number

        # Check if the number is a palindrome
        return number == reversed_half or number == reversed_half // 10
