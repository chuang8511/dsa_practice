# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.output = []
        
        def backtracking(new_nums: list[int], remaining_nums: list[int]):
            if len(new_nums) == len(nums):
                self.output.append(new_nums)
            else:
                for num in remaining_nums:
                    new_remaining = remaining_nums.copy()
                    new_remaining.remove(num)
                    backtracking(new_nums + [num], new_remaining)
        backtracking([], nums)

        return self.output
    

test_cases = [
    [1,2,3],
    [0,1],
    [1]
]

solution = Solution()

for case in test_cases:
    print(solution.permute(case))