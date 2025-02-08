class Solution:
    '''
    make recursive calls for index i+2 and i+3 and
    maximise sum form left or right subree of recusrsive calls
    return max from index 0 and 1
    '''
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [-1 for i in range(n)]
        def fun(i):
            if i >= n:
                return 0
            if dp[i] == -1:
                dp[i] = nums[i]+max(fun(i+2), fun(i+3))
            return dp[i]

        ans = max(fun(0), fun(1))
        return ans
