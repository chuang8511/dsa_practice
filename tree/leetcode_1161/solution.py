# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: [TreeNode]) -> int:
        self.maxi = float("-inf")
        self.level = 0
        self.cur_sum = 0
        self.res = 0

        que = collections.deque()
        que.append(root)

        while que:
            self.level += 1
            self.cur_sum = 0

            que_len = len(que)
            for _ in range(que_len):
                node = que.popleft()
                if node is not None:
                    self.cur_sum += node.val
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
            # print(f"cur sum: {self.cur_sum}")
            # print(f"max: {self.maxi}")
            # print(f"level: {self.level}")
            # print(f"res: {self.res}")
            if self.maxi < self.cur_sum:
                self.maxi = self.cur_sum
                self.res = self.level
        
        return self.res