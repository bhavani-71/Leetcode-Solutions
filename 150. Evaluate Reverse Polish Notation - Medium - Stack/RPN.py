from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Stack to keep operands
        
        for token in tokens:
            # If the token is a number, convert it to integer and push onto stack
            if token not in '+-*/':
                stack.append(int(token))
            else:
                # If the token is an operator, pop top two operands
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                # Apply the operator and push the result back to the stack
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    # Use int() to ensure the result truncates toward zero
                    stack.append(int(operand1 / operand2))
        
        # The final result is the only element left in the stack
        return stack[0]
