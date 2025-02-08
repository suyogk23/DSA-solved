class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        nums_0 = nums[:n-1]
        nums_n = nums[1:]
        dp_0 = [-1 for i in range (n-1)]
        dp_n = [-1 for i in range (n-1)]

        return max(self.fun(len(nums_0)-1, dp_0, nums_0), self.fun(len(nums_n)-1, dp_n, nums_n))

    def fun(self, i, dp, nums):
        if i < 0:
            return 0
        if(dp[i]==-1):
            dp[i] = max(self.fun(i-1, dp, nums), nums[i] + self.fun(i-2, dp, nums))
        return dp[i]


