class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        lheap, rheap = [], []
        l, r = 0, n-1
        ans = 0
        while(k > 0):
            while(len(lheap) < candidates and l <= r):
                heapq.heappush(lheap, costs[l])
                l+=1
            while(len(rheap) < candidates and r >= l):
                heapq.heappush(rheap, costs[r])
                r-=1
            # print(lheap, rheap)
            if not rheap:
                ans += heapq.heappop(lheap)
            elif not lheap:
                ans += heapq.heappop(rheap)
            elif (lheap[0] <= rheap[0]):
                ans += heapq.heappop(lheap)
            else:
                ans += heapq.heappop(rheap)
            k -= 1
        return ans
