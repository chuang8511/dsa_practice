class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.output = []
        def backtracking(combination: str, next_digits: str):
            if len(next_digits) == 0:
                self.output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtracking(combination+letter, next_digits[1:])

        backtracking("", digits)

        return self.output
    

test_cases = [
    "23",
    "",
    "2"
]

solution = Solution()
for case in test_cases:
    print(solution.letterCombinations(case))