# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[[ListNode]]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy

        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                val = node.val
                heapq.heappush(min_heap, (val, idx, node))
        
        while min_heap:
            _, idx, node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next