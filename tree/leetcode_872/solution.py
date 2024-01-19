# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: [TreeNode], root2: [TreeNode]) -> bool:
        # DFS with lower time complexity
        # stack_1 = [root1]
        # stack_2 = [root2]
        # root1_leave = None

        # while stack_1:
        #     node = stack_1.pop()
        #     if node:
        #         if node.left or node.right:
        #             stack_1.append(node.left)
        #             stack_1.append(node.right)
        #         else:
        #             root1_leave = node.val
            
        #     if root1_leave:
                
        #         while stack_2:
        #             node = stack_2.pop()
        #             if node:
        #                 if node.left or node.right:
        #                     stack_2.append(node.left)
        #                     stack_2.append(node.right)
        #                 else:
        #                     if root1_leave == node.val:
        #                         root1_leave = None
        #                         break
        #                     else:
        #                         return False
        # if root1_leave is None:
        #     while stack_2:
        #         node = stack_2.pop()
        #         if node:
        #             return False
        #     return True
        # else:
        #     return False
        
        # DFS with simple code
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)