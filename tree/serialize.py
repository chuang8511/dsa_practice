# Need to solve it again!

# Definition for a binary tree node.
import collections
# Need to understand pre-order traversal.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



    # It was my wrong answer.
    # I will come back to check why it is wrong later.
    # def serialize(self, root):
    #     queue = collections.deque()
    #     queue.append(root)
    #     encodedString = ""

    #     while queue:
    #         lenQueue = len(queue)
    #         for _ in range(lenQueue):
    #             node = queue.popleft()
    #             if node:
    #                 encodedString += str(node.val)
    #                 queue.append(node.left)
    #                 queue.append(node.right)
    #             else:
    #                 encodedString += "N"
        
    #     return encodedString


    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
        

    # def deserialize(self, data):
    #     queue = collections.deque()
    #     tree = TreeNode(0)
    #     queue.append(tree)
    #     idx = 0
    #     lenData = len(data)
    #     while queue:
    #         node = queue.popleft()
    #         if node:
    #             if data[idx] != "N":
    #                 node.val = int(data[idx])
    #                 leftIdx = 2 * idx + 1
    #                 rightIdx = 2 * idx + 2
    #                 if leftIdx < lenData and data[leftIdx] != "N":
    #                     leftNode = TreeNode(int(data[leftIdx]))
    #                     node.left = leftNode
    #                 if rightIdx < lenData and data[rightIdx] != "N":
    #                     rightNode = TreeNode(int(data[rightIdx]))
    #                     node.right = rightNode
    #                 queue.append(leftNode)
    #                 queue.append(rightNode)
    #                 idx += 1
    #             else:
    #                 idx += 1
    #     return tree
        
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))