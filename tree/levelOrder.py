# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: [TreeNode]) -> list[list[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            values = []
            for _ in range(queueLength):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    values.append(node.val)
            if values:
                res.append(values)
        return res