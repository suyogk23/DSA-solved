class Solution:
    # solution by @suyogk23 GITHUB
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq, i)
            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]
        
