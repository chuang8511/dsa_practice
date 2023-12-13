# Definition for singly-linked list.
# The solution is different from NeetCode!
# todo: please try to do solution like NeetCode. It is much easier
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

    # def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
    #     reversedList = self.reverseList(head)
    #     if n == 1:
    #         reversedList = reversedList.next
    #         return self.reverseList(reversedList)
    #     else:
    #         dum = reversedList
    #         for _ in range(n-1):
    #             beforeDeleteNode = dum
    #             deleteNode = dum.next
    #             dum = dum.next
    #         temp = deleteNode.next
    #         beforeDeleteNode.next = temp
    #         return self.reverseList(reversedList)

    #     # return

    # def reverseList(self, list: [ListNode]):
    #     prev = None
    #     while list:
    #         temp = list.next
    #         list.next = prev
    #         prev = list
    #         list = temp
    #     return prev
        
        # nodeCount = 0
        # dum = head
        # while dum:
        #     nodeCount += 1
        #     dum = dum.next
            
        # if nodeCount == n:
        #     head = head.next
        #     return head

        # targetMoveCount = nodeCount - n - 1    
        # if targetMoveCount == 0:
        #     head.next = None
        #     return head
        # else:
        #     dum = head
        #     for _ in range(targetMoveCount):
        #         targetNode = dum.next
        #         dum = dum.next
            
        #     temp = targetNode.next.next
        #     targetNode.next = temp
        #     return head

# arr = [1, 2, 3, 4, 5]
# n = 2

# arr = [1]
# n = 1

# arr = [1, 2]
# n = 1

# arr = [1, 2]
# n = 2

arr = [1,2,3]
n = 2

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
result = solution.removeNthFromEnd(head, n)

class TraverseList:
    def print(head: ListNode):
        print("========")
        while head:
            print(head.val)
            head = head.next

TraverseList.print(result)