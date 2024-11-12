# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end
# @param {ListNode} head
# @return {ListNode}
def delete_middle(head)
    if head.next.nil?
        return nil
    end

    node_count = 0
    node = head
    while node
        node_count += 1
        node = node.next
    end
    mid = node_count / 2

    node = head
    while mid > 1
        node = node.next
        mid -= 1
    end
    next_next = node.next.next

    node.next = next_next
    return head    
end

class BuildListNode
    def build(nums)
        node = ListNode.new()
        tail = node
        for num in nums
            new_node = ListNode.new(val = num)
            tail.next = new_node
            tail = tail.next
        end
        return node.next
    end
    def traverse(head)
        nums = []
        while head
            nums.append(head.val)
            head = head.next
        end
        return nums
    end
end

test_cases = [
    [1,3,4,7,1,2,6],
    [1,2,3,4],
    [2,1]
]

builder = BuildListNode.new()
for test_case in test_cases
    head = builder.build(test_case)
    result = delete_middle(head)
    print(builder.traverse(result), "\n")
end
