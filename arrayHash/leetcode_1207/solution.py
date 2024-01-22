from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dict = defaultdict(int)
        for i in arr:
            dict[i] += 1
        
        return len(dict.values()) == len(set(dict.values()))