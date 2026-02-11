class MedianFinder:
    # maintian a balanced left min and right max heap, with n/2 elements each
    # when there is an odd num of element, push the extra element to left min heap instead

    def __init__(self):
        self.left_min_heap = [] # left n/2 - 1 elements
        self.right_max_heap = [] # right n/2 + 1 elements

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.right_max_heap, -num)
        max_top = heapq.heappop(self.right_max_heap)
        heapq.heappush(self.left_min_heap, -max_top)

        if len(self.left_min_heap) > 1 + len(self.right_max_heap):
            min_top = heapq.heappop(self.left_min_heap)
            heapq.heappush(self.right_max_heap, -min_top)

    def findMedian(self) -> float:
        n = len(self.left_min_heap) + len(self.right_max_heap)
        if n % 2 == 0:
            # even
            min_top = self.left_min_heap[0]
            max_top = -self.right_max_heap[0]
            return (min_top + max_top)/2
        else:
            min_top = self.left_min_heap[0]
            return min_top

'''
pattern Core idea: 
*
* *
*   *           
*  *  *.        *   
      ^         * *
      |         *   *
    min top     *  *  *.
                ^
                |
              max top
[MIN HEAP]  <>   [MAX HEAP]
'''
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
