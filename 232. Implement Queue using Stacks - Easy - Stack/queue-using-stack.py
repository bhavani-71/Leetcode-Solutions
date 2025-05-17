class MyQueue:

    def __init__(self):
        # Two stacks:
        # stack_in for enqueue operation (push)
        # stack_out for dequeue operation (pop and peek)
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Push element onto stack_in (enqueue)
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the current front element
        self.peek()
        # Pop and return the element from stack_out (dequeue)
        return self.stack_out.pop()

    def peek(self) -> int:
        # If stack_out is empty, pour all elements from stack_in to stack_out
        # This reverses order to simulate queue behavior
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Return the front element of the queue (last of stack_out)
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out
