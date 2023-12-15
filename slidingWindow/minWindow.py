from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCount = defaultdict(int)
        for c in t:
            targetCount[c] += 1
        
        l = 0
        res = ""

        for r in range(len(s)):
            targetCount[s[r]] -= 1

            while max(targetCount.values()) == 0:
                if len(res) > r - l + 1 or res == "":
                    res = s[l:r+1]
                targetCount[s[l]] += 1
                l += 1
                
        # print(res)
        return res
    
solution = Solution()

test_cases = [
    { "s": "ADOBECODEBANC", "t": "ABC" },
    { "s": "a", "t": "a" },
    { "s": "a", "t": "aa" },
    { "s": "cabwefgewcwaefgcf", "t": "cae" },
]
for test_case in test_cases:
    print(solution.minWindow(test_case["s"], test_case["t"]))