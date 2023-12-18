# Need to solve it again!

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

        # m = len(board[0])
        # n = len(board)
       
        # for y in range(n):
        #    for x in range(m):
        #        if board[y][x] in root.children:
        #             visited = []
        #             visited.append([x, y])
        #             directions = [[x - 1, y - 1],
        #                             [x - 1, y + 1],
        #                             [x + 1, y - 1],
        #                             [x + 1, y + 1]]
        #             root = root.children[board[y][x]]

        #             for direction in directions:
        #                 x1 = direction[0]
        #                 y1 = direction[1]
        #                 if x1 > 0 and x1 <= m and y1 > 0 and y1 <= n and [x1, y1] not in visited:
        #                     if board[y1][x1] in root.children:
