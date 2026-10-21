from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:        
        groups = defaultdict(list)
        for str_ in strs:
            counts = [0] * 26
            for ch in str_:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(str_)
        return list(groups.values())



if __name__ == "__main__":
    cases = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]

    for input_, expected in cases:
        result = Solution().groupAnagrams(input_)
        for r in result:
            r.sort()
        result.sort()
        for e in expected:
            e.sort()
        expected.sort()
        if result != expected:
            raise AssertionError(f"case: {input_}, result: {result}, expect: {expected}")
    print("All tests passed")