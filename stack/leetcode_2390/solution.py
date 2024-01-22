class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c != "*":
                res.append(c)
            else:
                res.pop()
        return "".join(res)