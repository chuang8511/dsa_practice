from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        self.res = ""
        dict = defaultdict(int)

        for c in t:
            dict[c] += 1

        l = 0

        for r in range(len(s)):
            dict[s[r]] -= 1
            while max(dict.values()) == 0:
                if len(self.res) > r - l + 1 or self.res == "":
                    self.res = s[l:r+1]
                dict[s[l]] += 1
                l += 1
        return self.res