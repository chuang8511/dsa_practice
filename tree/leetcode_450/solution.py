# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        
        def find_node(node):
            prev = None
            replace_direction = ""
            while node:
                if node.val < key:
                    prev = node
                    replace_direction = "right"
                    node = node.right
                elif node.val > key:
                    prev = node
                    replace_direction = "left"
                    node = node.left
                else:
                    return [prev, node, replace_direction]
            return [None, None, None]
        
        prev, key_node, replace_direction = find_node(root)
        
        if not key_node:
            return root
        
        if prev is None and root == key_node and replace_direction == "":
            if key_node.right:
                head = key_node.right
                deepest_node = key_node.right
                while deepest_node.left:
                    deepest_node = deepest_node.left
                deepest_node.left = key_node.left
                return head
            elif key_node.left:
                return key_node.left
            else:
                return None                

        if replace_direction == "right":
            if key_node.left:
                prev.right = key_node.left
                deepest_node = key_node.left
                while deepest_node.right:
                    deepest_node = deepest_node.right
                deepest_node.right = key_node.right
            elif key_node.right:
                prev.right = key_node.right
            else:
                prev.right = None

        elif replace_direction == "left":
            if key_node.right:
                prev.left = key_node.right
                deepest_node = key_node.right
                while deepest_node.left:
                    deepest_node = deepest_node.left
                deepest_node.left = key_node.left
            elif key_node.left:
                prev.left = key_node.left
            else:
                prev.left = None
        return root