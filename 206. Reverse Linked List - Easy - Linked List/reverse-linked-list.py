# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize previous node as None
        current = head  # Start from the head of the list
        
        while current:
            nextn = current.next  # Store next node temporarily
            current.next = prev  # Reverse the link
            prev = current  # Move prev pointer to current node
            current = nextn  # Move to next node
        
        return prev  # Prev becomes the new head of reversed list
