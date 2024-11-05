# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: [ListNode]) -> int:
        nums = []
        while head:
            val = head.val
            nums.append(val)
            head = head.next
        
        l, r = 0, len(nums) - 1

        max_twin = float("-inf")
        while l < r:
            max_twin = max(max_twin, nums[l] + nums[r])

            l += 1
            r -= 1
        
        return max_twin