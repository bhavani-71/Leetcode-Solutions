```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_pointer = fast_pointer = head

        # Step 1: Detect if cycle exists using two pointers
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next           # Move slow by 1 step
            fast_pointer = fast_pointer.next.next      # Move fast by 2 steps

            if slow_pointer == fast_pointer:
                # Step 2: Find the start node of the cycle
                start_pointer = head
                while start_pointer != slow_pointer:
                    start_pointer = start_pointer.next
                    slow_pointer = slow_pointer.next
                return start_pointer  # Cycle start node found

        return None  # No cycle found
```
