class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # BOTTOM UP
        n = len(nums)
        dp = [1] * (n)
        # ans = -float('inf')
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])                    
            # ans = max(ans, dp[i])
        ans = max(dp) # both method works
        return ans

        # TOP DOWN (does not work in LC)
        # dp = {}
        # def dfs(i, prev):
        #     if i == n:
        #         return 0
        #     take = 0
        #     if (i, prev) in dp:
        #         return dp[(i, prev)]
        #     if nums[i] > prev:
        #         take = 1 + dfs(i+1, nums[i])
        #     not_take = dfs(i+1, prev)
        #     dp[(i, prev)] = max(take, not_take)
        #     return dp[(i, prev)]
        # return dfs(0, -float('inf'))
