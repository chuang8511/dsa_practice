class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end

class BuilderTreeNode
    def build(nums)
        return nil if nums.length == 0
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