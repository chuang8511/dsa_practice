# Need to solve it again!

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:        
    def __init__(self) -> None:
        self.max_ans = float("-inf")

    def maxPathSum(self, root: [TreeNode]) -> int:  
        # return max path sum wiht no split.
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            l = max(0, l)
            r = max(0, r)

            # set the max path sum with split
            self.max_ans = max(self.max_ans, root.val + l + r)
            
            return root.val + max(l, r)
        
        helper(root)
        
        return self.max_ans