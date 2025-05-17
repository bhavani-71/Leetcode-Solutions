class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold opening brackets
        stackOfOpen = []
        
        # Hash map to match each closing bracket to its corresponding opening bracket
        hashmap = {')': '(', '}': '{', ']': '['}

        # Iterate over each character in the input string
        for i in s:
            # If character is a closing bracket
            if i in hashmap:
                # If stack is empty or top of the stack doesn't match the corresponding opening bracket
                if not stackOfOpen or hashmap[i] != stackOfOpen[-1]:
                    return False  # String is invalid
                
                # Pop the matched opening bracket from stack
                stackOfOpen.pop()
            else:
                # If character is an opening bracket, push it onto the stack
                stackOfOpen.append(i)

        # If stack is empty, all brackets were properly closed; else invalid
        return not stackOfOpen
