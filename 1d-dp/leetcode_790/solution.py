# Please draw the image to think.
# Ref: https://leetcode.com/problems/domino-and-tromino-tiling/solutions/1620809/python-java-c-c-dp-image-visualized-explanation-100-faster-o-n
# dp equation: dp[i] = 2 * dp[i-1] + dp[i-3]
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,2,5] + [0] * (n - 3)

        for i in range(3, n):
            dp[i] = (2 * dp[i-1] + dp[i-3]) 

        return dp[n-1] % (1000000007)