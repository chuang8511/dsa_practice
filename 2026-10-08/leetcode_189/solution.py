class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) == 0:
            return
        k = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        
        
        



        

if __name__ == "__main__":
    cases = [
        ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
        ([-1,-100,3,99], 2, [3,99,-1,-100])
    ]

    for nums, k, result in cases:
        Solution().rotate(nums, k)
        if result != nums:
            raise AssertionError(f"case: {nums}, k: {k}")
    print("All tests passed")