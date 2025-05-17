class Solution:
    def addBinary(self, binary1: str, binary2: str) -> str:
        result = ""           # To store the binary sum result
        carry = 0             # Carry from previous addition

        # Start from the last index of each binary string
        index1, index2 = len(binary1) - 1, len(binary2) - 1

        # Loop until both strings are fully traversed and no carry remains
        while index1 >= 0 or index2 >= 0 or carry:
            current_sum = carry  # Start with the carry

            # Add bit from binary1 if available
            if index1 >= 0:
                current_sum += int(binary1[index1])
                index1 -= 1

            # Add bit from binary2 if available
            if index2 >= 0:
                current_sum += int(binary2[index2])
                index2 -= 1

            # Current bit to add to result (0 or 1)
            result = str(current_sum % 2) + result

            # Calculate carry for next iteration (0 or 1)
            carry = current_sum // 2

        return result
