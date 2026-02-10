class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # maintain a sliding window, traverste left to right, expand and shrink it as the budget increase
        # use hashmap to trach occurance of element and heap to get max element
        # TC: O(n log n) n for linear traversal and log n for heap operations (push and pop)
        # Space: O(n)
        n = len(chargeTimes)
        ans = 0
        # max(chargeTimes) + k * sum(runningCosts)
        hm = defaultdict(int)
        pq = []
        cost = 0
        cur_max = 0
        left = 0
        for i in range(n):
            heapq.heappush(pq, -chargeTimes[i])
            hm[chargeTimes[i]] += 1
            cost += runningCosts[i]
            if pq:
                cur_budget = -pq[0] + (i-left+1)*cost
            while left <= i and cur_budget > budget:
                cost -= runningCosts[left]
                time = chargeTimes[left]
                hm[time] -= 1
                while pq and hm[-pq[0]] == 0: # lazy deletion
                    heapq.heappop(pq)
                left += 1
                if pq and left <= i:
                    cur_budget = -pq[0] + (i-left+1)*cost
            if cur_budget <= budget:
                ans = max(ans, (i-left+1))  
        
        return ans


                    

