# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, at the head
        slow = fast = head
        
        # Move fast pointer two steps and slow pointer one step at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast pointer reaches end, slow is at middle
        return slow
