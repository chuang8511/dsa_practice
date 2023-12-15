import heapq
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Because it is the BST, we can directly use DFS to get the answer iteratively.
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


# with heap & BFS
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        heap = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            queLen = len(queue)

            for _ in range(queLen):
                node = queue.popleft()
                if node:
                    heapq.heappush(heap, node.val)
                    queue.append(node.left)
                    queue.append(node.right)

        for _ in range(k):
            ans = heapq.heappop(heap)
        
        return ans