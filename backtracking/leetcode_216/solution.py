class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if k > n:
            return []
        elif k == n:
            return [1] * n
        
        self.res = []
        def backtrack(remain_k, remain_n, cur_list, usable_nums):
            print(f"re k: {remain_k}, re n: {remain_n}, list: {cur_list}, usable_nums: {usable_nums}")
            print(f"ans: {self.res}")
            print("============")
            
            if remain_k == 0 and remain_n == 0:
                res = cur_list.copy()
                self.res.append(res)
                return
            
            if (remain_k == 0 and remain_n != 0) or remain_k < 0 or remain_n < 0 or not usable_nums:
                return
            
            for i in usable_nums:
                if cur_list and cur_list[-1] > i:
                    continue

                remain_k -= 1
                remain_n -= i                
                nums = usable_nums.copy()
                
                nums.remove(i)
                if remain_k >= 0 and remain_n >= 0:
                    cur_list.append(i)
                    backtrack(remain_k, remain_n, cur_list, nums)
                    cur_list.remove(i)
                    remain_k += 1
                    remain_n += i
        
        backtrack(k, n, [], list(range(1, 10)))
        return self.res