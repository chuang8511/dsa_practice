class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        for c in range(COLS):
            l = []
            for r in range(ROWS):
                l.append(grid[r][c])
            # print(l)
            for idx in range(len(grid)):
                if grid[idx] == l:
                    res += 1

        return res