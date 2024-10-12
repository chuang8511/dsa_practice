from tree_node import TreeNode, BuildTreeNode

class Solution:
    # Recursive
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        def inorder(node: TreeNode, result: list[int]):
            if node is not None:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)
        
        result = []
        inorder(root, result)

        return result
    
    # Iterative
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        stack = []

        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)

            current = current.right
        
        return result
    


test_cases = [
    [1,None,2,3],
    [1,2,3,4,5,None,8,None,None,6,7,9],
    [],
    [1]
]

solution = Solution()
for case in test_cases:
    tree = BuildTreeNode().build(case)
    print(solution.inorderTraversal(tree))
