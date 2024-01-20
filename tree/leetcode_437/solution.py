# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: [TreeNode], targetSum: int) -> int:
        res = [0]
        
        def dfs(node, possible_numbers):
            if not node:
                return

            remainings = possible_numbers.copy()
            remainings.append(targetSum)
            # print(f"node value: {node.val}")
            # print(f"remainings: {remainings}")
            # print(f"pos: {node.possible_numbers}")
            
            
            if node.val in remainings:
                res[0] += remainings.count(node.val)
                # print(f"res: {res[0]}")
            
            if node.left or node.right:
                for k, v in enumerate(remainings):
                    remainings[k] = v - node.val
            
            if node.left:
                dfs(node.left, remainings)
            
            if node.right:
                dfs(node.right, remainings)
        
        dfs(root, [])

        return res[0]