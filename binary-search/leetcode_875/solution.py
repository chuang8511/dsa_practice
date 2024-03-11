import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            eat_time = 0
            for pile in piles:
                eat_time += math.ceil(pile / mid)

                if eat_time > h:
                    break
            
            if eat_time <= h:
                right = mid
            else:
                left = mid + 1
        
        return right