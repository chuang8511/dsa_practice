class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.output = []
        def backtracking(chosen_candidates: list[int], candidates: list[int], target: int):
            if target == 0:
                self.output.append(chosen_candidates)
            else:
                for i, candidate in enumerate(candidates):
                    if target > 0:
                        backtracking(chosen_candidates + [candidate], candidates[i:], target - candidate)
        
        backtracking([], candidates, target)

        return self.output
    


test_cases = [
    {
        "candidates": [2,3,6,7],
        "target": 7
    },
    {
        "candidates": [2,3,5],
        "target": 8
    },
    {
        "candidates": [2],
        "target": 1
    },
]


solution = Solution()
for case in test_cases:
    print(solution.combinationSum(case["candidates"], case["target"]))