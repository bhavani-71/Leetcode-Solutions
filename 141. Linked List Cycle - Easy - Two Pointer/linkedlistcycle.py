# Definition for singly-linked list.
# Each node has a value and a reference to the next node.
# Example: 3 -> 2 -> 0 -> -4 (and cycle linking -4 to 2)

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head  # slow pointer moves one step at a time
        fast = head  # fast pointer moves two steps at a time

        # Traverse the list until fast pointer reaches the end or cycle is found
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If slow and fast meet, cycle exists
            if slow == fast:
                return True
        # If fast pointer reaches None, no cycle
        return False
