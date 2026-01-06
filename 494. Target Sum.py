class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, target):
            if i > n:
                return 0
            if i == n:
                if target != 0:
                    return 0
                else:
                    return 1
            if (i, target) in dp:
                return dp[(i, target)]
            plus = dfs(i+1, target-nums[i])
            minus = dfs(i+1, target+nums[i])
            dp[(i, target)] = plus+minus
            return dp[(i, target)]
        return dfs(0, target)
            

            
