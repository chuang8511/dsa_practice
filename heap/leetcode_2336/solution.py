import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.min_num = 1
        self.is_val_in_heap = {}
        self.heap = []

    def popSmallest(self) -> int:
        if not self.heap:
            smallest = self.min_num
            self.min_num += 1
        else:
            smallest = heapq.heappop(self.heap)
            del self.is_val_in_heap[smallest]
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.is_val_in_heap or num >= self.min_num:
            pass
        elif num == self.min_num - 1:
            self.min_num -= 1
        else:
            self.is_val_in_heap[num] = True
            heapq.heappush(self.heap, num)
        return


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)