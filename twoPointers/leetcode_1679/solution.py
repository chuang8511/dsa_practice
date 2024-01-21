from collections import defaultdict
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        self.operation_count = 0
        # Solution 1 with more space but quicker
        remainings = defaultdict(int)
        nums_pointer = 0
        
        while nums_pointer < len(nums):
            # print(f"num idx: {nums_pointer}")
            # print(remainings)
            num = nums[nums_pointer]
            if remainings[num] == 0: # cannot find
                remainings[k - num] += 1
            else:
                remainings[num] -= 1
                self.operation_count += 1
            nums_pointer += 1
        return self.operation_count
    
        # Solution 2: sort the array and use two pointer