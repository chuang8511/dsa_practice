# Need to solve it with better way again
# Current way is (M * N)^2

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        def can_arrive_atlantic(r, c):
            if r in range(ROWS) and c == COLS - 1:
                return True
            if c in range(COLS) and r == ROWS - 1:
                return True
            return False
        
        def can_arrive_pacific(r, c):
            if r in range(ROWS) and c == 0:
                return True
            if r == 0 and c in range(COLS):
                return True
            return False


        def dfs(r, c):
            if can_arrive_atlantic(r, c):
                atlantic.append(True)
            if can_arrive_pacific(r, c):
                pacific.append(True)
            
            if atlantic and pacific:
                return
                
            if (r >= ROWS or c >= COLS or 
                (r, c) in visited
                ):
                return
            
            directions = [[r + 1, c], [r - 1, c], [r, c - 1], [r, c + 1]]
            visited.add((r, c))
            # if r == 0 and c == 25:
            #     pdb.set_trace()
            for direction in directions:
                if direction[0] >= ROWS or direction[0] < 0 or direction[1] >= COLS or direction[1] < 0:
                    continue
                if heights[r][c] >= heights[direction[0]][direction[1]]:
                    dfs(direction[0], direction[1])




        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                atlantic = []
                pacific = []
                dfs(r, c)
                
                if atlantic and pacific:
                   
                    res.append([r, c])

        return res
    

sol = Solution()

# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[2,1],[1,2]]
heights = [[4,10,10,16,8,4,11,13,10,6,3,3,4,18,10,2,18,6,12,11,15,2,3,2,11,19,14,12,14,2,19,1,10,11,6,15,2],[6,16,9,11,15,4,14,3,6,11,2,0,14,7,0,19,3,14,2,15,19,1,10,2,6,5,14,14,6,9,14,12,18,6,2,19,19],[0,11,0,17,3,8,3,1,11,7,17,8,16,6,5,0,13,7,10,14,7,15,1,7,11,18,0,4,6,5,7,10,17,6,8,0,13],[1,3,4,7,17,0,12,10,5,4,17,11,0,17,3,2,16,7,5,15,3,17,13,15,13,14,11,2,3,1,9,1,12,4,18,5,9]]


result = sol.pacificAtlantic(heights)
print(result)