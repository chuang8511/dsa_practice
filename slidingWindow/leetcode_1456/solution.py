class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        self.maxi = 0
        vol = ["a", "e", "i", "o", "u"]

        vol_count = 0
        for i in range(k):
            if s[i] in vol:
                vol_count += 1
        self.maxi = vol_count

        l, r = 0, k

        while r < len(s):
            if s[l] in vol:
                vol_count -= 1
            l += 1

            if s[r] in vol:
                vol_count += 1
            r += 1
            self.maxi = max(self.maxi, vol_count)
        
        return self.maxi