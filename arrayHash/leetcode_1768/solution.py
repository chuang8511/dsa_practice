class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        loop_times = max(len(word1), len(word2))

        for i in range(loop_times):
            if i < len(word1):
                res = res + word1[i]
            if i < len(word2):
                res = res + word2[i]
        return res
    