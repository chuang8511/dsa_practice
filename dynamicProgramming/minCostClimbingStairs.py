class Solution:
    # def minCostClimbingStairs(self, cost: list[int]) -> int:
    #     return min(self.getMinCost(cost, 0), self.getMinCost(cost, 1))
            
    # def getMinCost(self, cost: list[int], start) -> int:
    #     sumNum = cost[start]
    #     while start + 2 < len(cost):
    #         if cost[start+1] >= cost[start+2]:
    #             sumNum += cost[start+2]
    #             start += 2
    #         else:
    #             sumNum += cost[start+1]
    #             start += 1
    #     return sumNum
    # def minCostClimbingStairs(self, cost: list[int]) -> int:
        
    #     if len(cost) > 3:
    #         if self.minCostClimbingStairs(cost[:-2]) <= self.minCostClimbingStairs(cost[:-1]):
    #             return cost[-1] + self.minCostClimbingStairs(cost[:-2])
    #         else:
    #             return cost[-1] + self.minCostClimbingStairs(cost[:-1])
    #     elif len(cost) == 3:
    #         return min(cost[1], cost[0] + cost[2])
        
    #     elif len(cost) == 2:
    #         return min(cost[0], cost[1])
    #     else:
    #         return cost[0]

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])


test_cases = [
    [1,100,1,1,1,100,1,1,100,1],
    [10,15,20],
    [0,1,2,2],
    [0,0,0,1]
]
solution = Solution()

for test_case in test_cases:
    result = solution.minCostClimbingStairs(test_case)
    print(result)