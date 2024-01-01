class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        row_zero = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0