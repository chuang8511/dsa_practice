class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
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