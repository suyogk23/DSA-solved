class Solution:
    # take or not take problem, if take, call (i+2) + cur_house_money, else call (i+1)
    # use dp to speed up
    # solution by @suyogk23 GITHUB
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)

        def dfs(i):
            # base case 
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            # not take money from current house
            not_take = dfs(i+1)
            # take money from current house
            take = nums[i] + dfs(i+2)
            dp[i] = max(take, not_take)
            return dp[i]
        
        return dfs(0)
