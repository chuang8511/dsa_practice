# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return head
            
        odd, even, evenHead = head, head.next, head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next
        odd.next = evenHead

        return head