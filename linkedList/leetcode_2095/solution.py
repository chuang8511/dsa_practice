# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: [ListNode]) -> [ListNode]:
        list_length = 0
        temp = head
        while temp is not None:
            list_length += 1
            temp = temp.next

        if list_length == 1:
            return None
        if list_length == 2:
            head.next = None
            return head
        if list_length == 3:
            next_node = head.next.next
            head.next = next_node
            return head
        
        if list_length % 2 == 0:
            takeout_node_number = (list_length // 2) + 1
        else:
            takeout_node_number = (list_length + 1) // 2
        
        pre_node = head
        for _ in range(takeout_node_number - 2):
            pre_node = pre_node.next

        next_node = pre_node.next.next

        pre_node.next = next_node

        return head