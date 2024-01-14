class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            return (flowerbed[0] == 0 and n == 1)
        
        for idx, val in enumerate(flowerbed):
            if n == 0:
                return True

            if idx == 0:
                able_to_plant_here = (val == 0 and flowerbed[idx+1] == 0)
            elif idx == len(flowerbed) - 1:
                able_to_plant_here = (val == 0 and flowerbed[idx-1] == 0)
            else:
                able_to_plant_here = (val == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0)
            
            if able_to_plant_here:
                flowerbed[idx] = 1
                n -= 1
        
        return n == 0