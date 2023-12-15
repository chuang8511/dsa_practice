import pdb
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphCount = defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(s)):
            alphCount[s[r]] += 1
            
            while r - l + 1 - max(alphCount.values()) > k:
                alphCount[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


solution = Solution()
s = "ABAB"
k = 2

# s = "AABABBA"
# k = 1
s = "AAAA"
k = 2

s = "ABBB"
k = 2
s = "EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
k = 7
print(solution.characterReplacement(s, k))