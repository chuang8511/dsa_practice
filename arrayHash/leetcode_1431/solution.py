class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy_count = max(candies)
        res = []
        
        for i in candies:
            res.append(i+extraCandies >= max_candy_count)

        return res