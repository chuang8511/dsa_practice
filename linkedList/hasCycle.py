# It is kind of math problem.
# Please review it again later.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False       



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