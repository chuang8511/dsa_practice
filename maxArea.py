class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0 ,len(height) - 1
        max_size = 0

        while l < r:
            width = r - l
            water_height = min(height[r], height[l])
            size = width * water_height
            max_size = max(max_size, size)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

            
        return max_size
    

# height = [1,2,4,3]
# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]

solution = Solution()
print(solution.maxArea(height))