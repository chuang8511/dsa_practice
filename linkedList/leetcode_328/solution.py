# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        

        # fir_node = head
        # sec_node = head.next
        # pointer = 2
        # start_node = head.next.next
        # while start_node:
        #     if pointer % 2 == 0:
        #         fir_node.next.val = start_node.val
                

        #     else:
        #         sec_node.next = start_node
        #     pointer += 1
