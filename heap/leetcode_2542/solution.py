import heapq
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        res, sum, min_heap = 0, 0, []

        sorted_nums = sorted(list(zip(nums2, nums1)), key=lambda x: x[0], reverse=True)

        for n2, n1 in sorted_nums:
            sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) == k:
                res = max(res, sum * n2)
                sum -= heapq.heappop(min_heap)
        
        return res