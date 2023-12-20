# Need to solve it again!

import heapq

class MedianFinder:

    def __init__(self):
        # MinHeap
        self.largeHeap = []
        # MaxHeap
        self.smallHeap = []

    def addNum(self, num: int) -> None:
        # Logn
        heapq.heappush(self.smallHeap, -1 * num)

        if self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0]) > self.largeHeap[0]:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = -1 *heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, val)
        
    
    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return float(-1 * self.smallHeap[0])
        if len(self.largeHeap) > len(self.smallHeap):
            return float(self.largeHeap[0])
        return (-1 * self.smallHeap[0] + self.largeHeap[0]) / 2

# class MedianFinder:

#     def __init__(self):
#         self.largeHeap, self.smallHeap = []
        

#     def addNum(self, num: int) -> None:
#         heapq.heappush(self.heap, num)

#     def findMedian(self) -> float:
#         lenList = len(self.heap)

#         if lenList == 2:
#             res = sum(self.heap) / 2
#             return res
        
#         if lenList % 2 == 0:
#             idx = int((lenList) / 2)
#             res = 0

#             tempList = self.heap.copy()

#             for _ in range(idx - 1):
#                 heapq.heappop(tempList)
            
#             for _ in range(2):
#                 res += heapq.heappop(tempList)
#             return res / 2

            
#         else:
#             idx = int((lenList - 1) / 2)
#             tempList = self.heap.copy()
            
#             for _ in range(idx + 1):
#                 res = heapq.heappop(tempList)

#             return float(res)

        
mf = MedianFinder()
def addAndPrint(num):
    mf.addNum(num)
    res = mf.findMedian()
    print(res)

list = list(range(1, 11))

for i in list:
    addAndPrint(i)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()