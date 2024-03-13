class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        t_minus_3 = 0
        t_minus_2 = 1
        t_minus_1 = 1
        t_0 = t_minus_3 + t_minus_2 + t_minus_1

        if n == 3:
            return t_0
        
        for _ in range(n-3):
            temp = t_minus_2
            t_minus_3 = temp
            temp_ = t_minus_1
            t_minus_2 = temp_
            temp__ = t_0
            t_minus_1 = temp__
            t_0 = t_minus_3 + t_minus_2 + t_minus_1
        
        return t_0