class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        
        visit = set()
        res = []

        def dfs(r, c, i):
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] != word[i]
                ):
                return
            
            if i == len(word) - 1:
                res.append(True)
                return
            
            visit.add((r, c))
            i += 1
            dfs(r - 1, c, i)
            dfs(r + 1, c, i)
            dfs(r, c - 1, i)
            dfs(r, c + 1, i)
            i -= 1
            visit.remove((r, c))
        
        for row in range(ROWS):
            for col in range(COLS):
                if res:
                    return True
                else:
                    dfs(row, col, 0)
        return True if res else False

solution = Solution()

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = [["a"]]
# word = "ABCCED"
# word = "ABCB"
word = "a"
print(solution.exist(board, word))