
# Need to solve it again!
# after sorting, we can reduce the case count.
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # way1
        # def get_first_element(i):
        #     return i[0]

        # intervals.sort(key= get_first_element)
        # way2
        intervals.sort(key= lambda i : i[0])

        res = [intervals[0]]

        for start, end in intervals[1:]:
            previous_end = res[-1][1]

            if start <= previous_end:
                res[-1][1] = max(previous_end, end)
            else:
                res.append([start, end])
        return res