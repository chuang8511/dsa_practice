import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]:
        return
        

    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
         
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
    




class LinkedListBuilder:
    def build(self, arr=[int]):
        dum = ListNode()
        tail = dum
        for i in arr:
            node = ListNode(i)
            tail.next = node
            tail = tail.next
        return dum.next
    
class TraverseList:
    def print(head: ListNode):
        print("========")
        while head:
            print(head.val)
            head = head.next