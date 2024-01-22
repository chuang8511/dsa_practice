class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        self.highest = 0
        
        height = 0
        for num in gain:
            height += num
            self.highest = max(self.highest, height)
        
        return self.highest