# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end
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

class BuilderTreeNode
    def build(nums)
        data = nums.shift
        root = TreeNode.new(val=data)
        queue = [root]
        while queue.length > 0
            node = queue.shift
            if node
                data = nums.shift
                new_node1 = data.nil? ? nil : TreeNode.new(val=data)
                data = nums.shift
                new_node2 = data.nil? ? nil : TreeNode.new(val=data)
                queue.append(new_node1)
                queue.append(new_node2)
                node.left = new_node1
                node.right = new_node2
            end
        end
        return root
    end

    def traverse(root)
        queue = [root]
        nums = []
        while queue.length > 0 && queue.compact.length != 0
            node = queue.shift
            if node
                nums.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            elsif 
                nums.append(nil)
            end
        end
        return nums
    end
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