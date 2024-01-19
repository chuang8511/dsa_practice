import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        # Recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # Interative DFS
        # stack = [[root, 1]]
        # res = 0

        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         res = max(depth, res)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])

        # return res
    
        # BFS
        queue = collections.deque()
        
        if root:
            queue.append(root)

        depth = 0

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
            depth += 1
        return depth