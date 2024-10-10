class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        write = 0

        while i < len(chars):
            char = chars[i]
            count = 0

            while i < len(chars) and char == chars[i]:
                i += 1
                count += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for count_str in str(count):
                    chars[write] = count_str
                    write += 1
        
        print(chars)
        return write



test_cases = [
    ["a","a","b","b","c","c","c"],
    ["a"],
    ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
]

solution = Solution()
for case in test_cases:
    print(solution.compress(case))