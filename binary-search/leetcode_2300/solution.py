class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        if success <= 0:
            return [len(potions)] * len(spells)

        self.res = []
        sorted_potions = sorted(potions)
        
        for num in spells:
            l, r = 0, len(sorted_potions) - 1
            
            while l <= r:
                m = (l+r) // 2
                product = num * sorted_potions[m]

                if product < success:
                    l = m + 1
                else:
                    r = m - 1
        
            count = len(sorted_potions) - l
            self.res.append(count)

        return self.res