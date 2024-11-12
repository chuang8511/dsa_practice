require "../builder"
# @param {TreeNode} root
# @return {Integer[]}
def right_side_view(root)
    if root.nil?
        return []
    end

    if !root.left and !root.right
        return [root.val]
    end

    queue = [root]
    result = []
    while queue.length > 0
        node_count = queue.length
        for i in 1..node_count
            node = queue.shift
            if i == node_count
                result.append(node.val)
            end
            if node.left
                queue.append(node.left)
            end
            if node.right
                queue.append(node.right)
            end
        end
    end
    return result
end



test_cases = [
    {
        root: [1,2,3,nil,5,nil,4],
        expect: [1,3,4]
    },
    {
        root: [1,nil,3],
        expect: [1,3]
    },
    {
        root: [],
        expect: []
    },
    {
        root: [1,2],
        expect: [1,2]
    },
]

builder = BuilderTreeNode.new()
for test_case in test_cases
    root = builder.build(test_case[:root])
    result = right_side_view(root)

    if result == test_case[:expect]
        print("Pass!\n")
    else
        print("Not pass, result: #{result}\n")
    end
end