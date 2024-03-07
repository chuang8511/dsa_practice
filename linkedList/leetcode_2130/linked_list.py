
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedListBuilder:
    def build(self, arr=[int]):
        dum = ListNode()
        tail = dum
        for i in arr:
            node = ListNode(i)
            tail.next = node
            tail = tail.next
        return dum.next
    def debuild(self, linked_node=ListNode):
        arr = []
        temp = linked_node
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        return arr