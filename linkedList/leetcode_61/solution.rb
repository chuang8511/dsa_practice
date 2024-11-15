require "../build"
def rotate_right(head, k)
    return head if k == 0 or !head
    length = 0
    node = head
    while node
        length += 1
        node = node.next
    end

    if length == k or length == 1
        return head
    elsif length < k
        k = k % length
    end

    if k == 0
        return head 
    end

    times = length - k - 1
    target_node = head
    for i in 1..times
        target_node = target_node.next
    end
    result_node = target_node.next
    final_node = result_node
    if final_node
        while final_node.next
            final_node = final_node.next
        end
    end
    target_node.next = nil

    final_node.next = head

    return result_node    
end

builder = BuildListNode.new()

test_cases = [
    {
        head: [1,2,3,4,5], 
        k: 2,
        expect: [4,5,1,2,3],
    },
    {
        head: [0,1,2], 
        k: 4,
        expect: [2,0,1],
    },
    {
        head: [], 
        k: 1,
        expect: [],
    },
    {
        head: [1], 
        k: 99,
        expect: [1],
    },
    {
        head: [1,2,3,4,5], 
        k: 10,
        expect: [1,2,3,4,5],
    },
]

for test_case in test_cases
    list = builder.build(test_case[:head])
    result = rotate_right(list, test_case[:k])
    result_num = builder.traverse(result)
    if result_num == test_case[:expect]
        print("Pass!\n")
    else
        print("Not Pass, result: #{result_num}\n")
    end
end