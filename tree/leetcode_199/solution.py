# Definition for a binary tree node.
# import pdb
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: [TreeNode]) -> list[int]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            len_que = len(queue)
            rightest_val = None

            for i in range(len_que):
                node = queue.popleft()
                # pdb.set_trace()
                if node:
                    rightest_val = node.val
                    queue.append(node.left)
                    queue.append(node.right)

                if i == len_que - 1 and rightest_val is not None:
                    res.append(rightest_val)

        return res