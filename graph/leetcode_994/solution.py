import collections
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.time = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        rotten_oranges = []
        fresh_oranges  = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_oranges.append([r, c])
                elif grid[r][c] == 1:
                    fresh_oranges.append([r, c])
        
        if len(fresh_oranges) == 0:
            return 0
        
        if len(rotten_oranges) == 0:
            return -1

        que = collections.deque(rotten_oranges)

        while que and fresh_oranges:
            q_len = len(que)

            to_be_rotten = []
            for _ in range(q_len):
                r_, c_ = que.popleft()
                to_be_rotten.append([r_ + 1, c_])
                to_be_rotten.append([r_ - 1, c_])
                to_be_rotten.append([r_, c_ + 1])
                to_be_rotten.append([r_, c_ - 1])
            
            for rotten in to_be_rotten:
                if rotten in fresh_oranges:
                    fresh_oranges.remove(rotten)
                    que.append(rotten)

            self.time += 1
        return -1 if fresh_oranges else self.time