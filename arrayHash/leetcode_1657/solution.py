from collections import defaultdict
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for c in word1:
            d1[c] += 1

        for c in word2:
            d2[c] += 1

        return set(d1.keys()) == set(d2.keys()) and Counter(d1.values()) == Counter(d2.values())