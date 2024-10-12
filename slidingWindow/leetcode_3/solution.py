# "abcabcbb"
#    p p

# {
#    "a": 1,
#    "b": 1,
#    "c": 1
# }



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        count_dict = {}

        max_length = 0

        while r < len(s):
            if s[r] in count_dict:
                count_dict[s[r]] += 1
            else:
                count_dict[s[r]] = 1

            if count_dict[s[r]] == 1:
                max_length = max(max_length, r - l + 1)
            else:
                while l < r:
                    can_break = s[r] == s[l]
                    count_dict[s[l]] -= 1
                    l += 1
                    if can_break:
                        break
            r += 1
        
        return max_length
    

test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew"
]


solution = Solution()

for case in test_cases:
    print(solution.lengthOfLongestSubstring(case))
