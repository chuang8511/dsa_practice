# [1, 2]
# [1, 3]
# [1, 4]
# [2, 3]
# [2, 4]
# [3, 4]
# [4]
# [1, 2, 3]

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.output = []
        def backtracking(nums: list[int], target_length: int, range_nums: list[int]):
            if target_length == 0:
                self.output.append(nums)
            else:
                for num in range_nums:
                    backtracking(nums + [num], target_length - 1, range(num+1, n+1))
        
        backtracking([], k, range(1, n+ 1))

        return self.output
    

test_cases = [
    {
        "n": 3,
        "k": 3,
    },
    {
        "n": 4,
        "k": 2,
    },
    {
        "n": 1,
        "k": 1,
    }
]

solution = Solution()
for case in test_cases:
    print(solution.combine(case["n"], case["k"]))