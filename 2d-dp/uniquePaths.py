# Need to solve it again!
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            new_row = [1] * n

            for j in range(n - 1):
                new_row[j + 1] = new_row[j] + row[j + 1]
            row = new_row
        return row[n - 1]
    
m = 3
n = 7

solution = Solution()
res = solution.uniquePaths(m, n)
print(res)