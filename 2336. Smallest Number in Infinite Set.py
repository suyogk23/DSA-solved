"""
solution by @suyogk23 GITHUB
track the smallest number using a variable
if added number smaller than the smallest number variable, store these values in a heap and a set
- heap: to get the smallest values in O(1) time, add and remove in O(log n)
- set: to keep track of duplicates, find, insert and delete in O(1)
These 2 datastructures enable efficient operations in the object with 1 operation costing only O(log n) in worst case
"""
class SmallestInfiniteSet:

    def __init__(self):
        self.min_ele = 1
        self.pq = []
        self.s = set()

    def popSmallest(self) -> int:
        if len(self.pq) >= 1:
            val = self.pq[0]
            heapq.heappop(self.pq)
            self.s.remove(val)
            return val
        self.min_ele += 1
        return self.min_ele-1

    def addBack(self, num: int) -> None:
        if num < self.min_ele:
            if num not in self.s:
                heapq.heappush(self.pq, num)
                self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
