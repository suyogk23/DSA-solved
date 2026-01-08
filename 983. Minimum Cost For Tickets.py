class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # bottom up solution
        n = len(days)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(n):
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i
                while j < n and days[j] < duration + days[i]:
                    j+=1
                dp[j] = min(dp[j], cost + dp[i])
        return dp[n]
        # top down solution
        # n = len(days)
        # dp = [None]*(n+1)
        # def dfs(i):
        #     if i == n:
        #         return 0
        #     if dp[i]:
        #         return dp[i]
        #     res = float('inf')
        #     # 3 branches for each cost in every combination
        #     for cost, duration in zip(costs, [1, 7, 30]):
        #         j = i
        #         # for accounting the duration for which the pass lasts
        #         while j < n and days[j] < days[i] + duration:
        #             j += 1
        #         # minimize the cost cobination
        #         res = min(res, cost + dfs(j))
        #     dp[i] = res
        #     return dp[i]
        
        # return dfs(0)

