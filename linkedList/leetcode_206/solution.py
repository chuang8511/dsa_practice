# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return head
        
        next = head.next

        if not next:
            return head
        
        head.next = None
        cur = head

        while cur and next:
            next_next = next.next
            next.next = cur
            cur = next
            next = next_next
        
        return cur