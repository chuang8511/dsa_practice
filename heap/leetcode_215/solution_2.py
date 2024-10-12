import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = num * -1
        heapq.heapify(nums)

        for i in range(k):
            result = heapq.heappop(nums)
        result *= -1
        
        return result
    



test_cases = [
    {
        "nums": [3,2,1,5,6,4],
        "k": 2
    },
    {
        "nums": [3,2,3,1,2,4,5,5,6],
        "k": 4
    },
]


solution = Solution()
for case in test_cases:
    print(solution.findKthLargest(nums=case["nums"], k=case["k"]))