# To be used another way to express spiral
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        visited = set()
        ROWS = len(matrix)
        COLS = len(matrix[0])
        all_numbers_count = ROWS * COLS
        
        res = []

        row, col = 0, 0
        direction = "right"
        next_dir_dic = {
            "right": "down",
            "down": "left",
            "left": "up",
            "up": "right",
        }
        while len(res) < all_numbers_count:

            if ((row, col) not in visited 
                and row >= 0 and row < ROWS 
                and col >= 0 and col < COLS):
                res.append(matrix[row][col])
                visited.add((row, col))
                if direction == "right":
                    col += 1
                elif direction == "down":
                    row += 1
                elif direction == "left":
                    col -= 1
                elif direction == "up":    
                    row -= 1
            else:
                direction = next_dir_dic[direction]
                if direction == "right":
                    col += 1
                    row += 1
                elif direction == "down":
                    row += 1
                    col -= 1
                elif direction == "left":
                    col -= 1
                    row -= 1
                elif direction == "up":    
                    row -= 1
                    col += 1
        return res

solution = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res = solution.spiralOrder(matrix)
print(res)