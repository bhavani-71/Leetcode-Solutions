# Definition for singly-linked list.
# Each node has a value and a reference to the next node.
# Example: 1 -> 2 -> 4

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the head of the merged list
        l = ListNode(0)
        current = l  # Pointer to track the last node in the merged list

        # Loop until either list1 or list2 is exhausted
        while list1 and list2:
            # Compare current values and attach the smaller one
            if list1.val < list2.val:
                current.next = list1  # Point to list1's current node
                list1 = list1.next    # Move list1 forward
            else:
                current.next = list2  # Point to list2's current node
                list2 = list2.next    # Move list2 forward
            current = current.next    # Advance the current pointer

        # Attach the remaining nodes from whichever list is not empty
        current.next = list1 if list1 else list2

        # Return the merged list (skipping the dummy head)
        return l.next
