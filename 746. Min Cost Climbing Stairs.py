class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # brute force
        # def bfs(n):
        #     if n >= len(cost):
        #         return 0
        #     if n == -1:
        #         return  min(bfs(n+1), bfs(n+2))
        #     return cost[n] + min(bfs(n+1), bfs(n+2))

        # return bfs(-1)

        # top down
        dp = [-1 for i in range(len(cost))]

        def bfs(n):
            if n >= len(cost):
                return 0
            if (dp[n] != -1):
                return dp[n]
            if n == -1:
                return  min(bfs(n+1), bfs(n+2))
            dp[n] = cost[n] + min(bfs(n+1), bfs(n+2))
            return dp[n]
        return bfs(-1)

        # space optimized
        # for i in range(len(cost)-3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])

            
        