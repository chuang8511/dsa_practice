# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    hash = {}
    node = head

    while node
        if hash[node]
            return true
        else
            hash[node] = true
        end
        node = node.next
    end
    return false
end

