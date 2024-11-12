require "../builder"
# Definition for a binary tree node.

# @param {TreeNode} root
# @return {Integer}
def good_nodes(root)
    queue = [[root, root.val]]
    count = 0
    while queue.length > 0
        node, max = queue.shift
        count += 1 if node.val >= max
        queue.append([node.left, [node.left.val, max].max]) if node.left
        queue.append([node.right, [node.right.val, max].max]) if node.right
    end
    return count
end
test_cases = [
    {
        input: [3,1,4,3,nil,1,5],
        expected: 4
    },
    {
        input: [3,3,nil,4,2],
        expected: 3
    },
    {
        input: [1],
        expected: 1
    }
]

builder = BuilderTreeNode.new()
for test_case in test_cases
    root = builder.build(test_case[:input])
    result = good_nodes(root)

    if result != test_case[:expected]
        print("Not pass, result is #{result}\n")
    else
        print("Pass!\n")
    end
end