from tree_node import BuildTreeNode, TreeNode
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        queue = deque()
        result = []
        queue.append(root)
        while len(queue) > 0:
            process_time = len(queue)
            for i in range(process_time):
                node = queue.popleft()
                if i == process_time - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return result


test_cases = [
    [1,2,3,None,5,None,4],
    [1,None,3],
    []
]

solution = Solution()
for case in test_cases:
    tree = BuildTreeNode().build(case)
    print(solution.rightSideView(tree))


