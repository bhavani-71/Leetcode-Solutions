class MinStack:

    def __init__(self):
        # Stack to store all values
        self.main_stack = []
        # Stack to keep track of the minimum values
        self.min_stack = []        

    def push(self, value: int) -> None:
        self.main_stack.append(value)
        # Only push to min_stack if it's empty or the new value is <= current min
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)        

    def pop(self) -> None:
        removed_value = self.main_stack.pop()
        # Also pop from min_stack if it was the minimum
        if removed_value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top value from the main stack

        return self.main_stack[-1]

    def getMin(self) -> int:
        # Return the current minimum value
        return self.min_stack[-1]
