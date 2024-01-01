class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # O(logn n)
        # intervals.sort(key= lambda i : i[0])
        
        # res = 0
        # previous_interval = intervals[0]
        
        # # O(n)
        # for start, end in intervals[1:]:
        #     previous_end = previous_interval[1]

        #     # overlap
        #     if start < previous_end:
        #         res += 1
        #         if end < previous_end:
        #             previous_interval = [start, end]
        #     else:
        #         previous_interval = [start, end]
        # return res

        intervals.sort()

        res = 0
        pre_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= pre_end:
                pre_end = end
            else:
                res += 1
                pre_end = min(end, pre_end)

        return res
