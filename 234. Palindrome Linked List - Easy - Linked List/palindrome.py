class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        second_half_head = self.reverseList(slow)
        
        # Step 3: Compare the first half and reversed second half node by node
        first_half_node = head
        second_half_node = second_half_head
        while second_half_node:
            if first_half_node.val != second_half_node.val:
                return False
            first_half_node = first_half_node.next
            second_half_node = second_half_node.next
        
        # Optional Step 4: Restore the original list (reverse second half back)
        self.reverseList(second_half_head)
        
        return True
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
