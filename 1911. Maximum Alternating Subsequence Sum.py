class Solution:
    # solution by @suyogk23 GITHUB
    # maintain state and op(add/subtract) based on current state.
    # keep track of (index, op), op also because we need to store states if the current number is added in subsequenc and also current number is subtracted in subsequence
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
    
        dp = {}
        def dfs(i, op):
            if i >= n:
                return 0
            if (i, op) in dp:
                return dp[(i, op)]
            take = (nums[i]*op) + dfs(i+1, op*-1)
            not_take = dfs(i+1, op)
            dp[(i,op)] = max(take, not_take)
            return dp[(i, op)]
        
        return dfs(0, 1)
