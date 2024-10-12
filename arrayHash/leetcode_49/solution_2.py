class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result_dict = {}

        for str in strs:
            sorted_string = "".join(sorted(str))

            if sorted_string in result_dict:
                result_dict[sorted_string].append(str)
            else:
                result_dict[sorted_string] = [str]

        return result_dict.values()


test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
]

solution = Solution()

for case in test_cases:
    print(solution.groupAnagrams(strs=case))