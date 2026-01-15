class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_prd = max_prd = ans = nums[0]
        for i in range(1, n):
            prev_min = min_prd
            prev_max = max_prd
            min_prd = min(nums[i], nums[i]*prev_min, nums[i]*prev_max)
            max_prd = max(nums[i], nums[i]*prev_min, nums[i]*prev_max)
            print(min_prd, max_prd)
            ans = max(ans, max_prd)

        return ans


'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = {}
        def dfs(i, prd):
            if i == n:
                return prd
            if (i, prd) in dp:
                return dp[(i, prd)]
            take = dfs(i+1, prd*nums[i])
            not_take = dfs(i+1, nums[i])
            dp[(i, prd)] = max(take, not_take, prd)
            return dp[(i, prd)]
        return dfs(1, nums[0])
'''
