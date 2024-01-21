class Solution:
    def maxArea(self, height: list[int]) -> int:
        self.max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            self.max_area = max(self.max_area, h * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return self.max_area