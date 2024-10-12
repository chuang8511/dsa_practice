class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        array_dict = []
        result = []
        
        for str in strs:
            count_dict = {}

            for cha in str:
                if cha in count_dict:
                    count_dict[cha] += 1
                else:
                    count_dict[cha] = 1
            
            if count_dict in array_dict:
                idx = array_dict.index(count_dict)
                result[idx].append(str)
            else:
                array_dict.append(count_dict)
                result.append([str])
        
        return result
        
    

test_cases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
]

solution = Solution()

for case in test_cases:
    print(solution.groupAnagrams(strs=case))