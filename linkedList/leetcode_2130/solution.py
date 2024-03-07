# Definition for singly-linked list.
from collections import defaultdict
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: [ListNode]) -> int:
        idx_dict = defaultdict(int)
        i = 0
        temp = head
        while temp:
            idx_dict[i] = temp.val
            temp = temp.next
            i += 1
        
        l, r = 0, i - 1
        max_sum = float("-inf")

        while l < r:
            sum_pair = idx_dict[l] + idx_dict[r]
            max_sum = max(sum_pair, max_sum)
            l += 1
            r -= 1
        
        return max_sum