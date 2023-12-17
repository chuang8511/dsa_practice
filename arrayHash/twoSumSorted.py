class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r and target != numbers[l] + numbers[r]:
            # print(f"sum: #{numbers[l] + numbers[r]}")
            # print(f"l: #{l}")
            # print(f"r: #{r}")
            if target > numbers[l] + numbers[r]:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]

solution = Solution()

numbers = [2,7,11,15]
target = 9
print(solution.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(solution.twoSum(numbers, target))

numbers = [5,25,75]
target = 100
print(solution.twoSum(numbers, target))