import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 

        # memory: O(N), speed: O(N)
        # values = []
        # while head:
        #     values.append(head.val)
        #     head = head.next
        # l, r = 0, len(values) - 1
        
        # dummy = ListNode()
        # tail = dummy
        
        # while l < r:
        #     node2 = ListNode(values[r])
        #     node1 = ListNode(values[l], node2)
        #     tail.next = node1
        #     tail = tail.next.next
        #     l += 1
        #     r -= 1
        
        # head = dummy.next
        # """
        # Do not return anything, modify head in-place instead.
        # """
        
arr = [1, 2, 3, 4]

class LinkedListBuilder:
    def build(self, arr=[int]):
        dum = ListNode()
        tail = dum
        for i in arr:
            node = ListNode(i)
            tail.next = node
            tail = tail.next
        return dum.next

head = LinkedListBuilder().build(arr)
solution = Solution()
solution.reorderList(head)