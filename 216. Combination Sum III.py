class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # soultion by @suyogk23 GITHUB
        # recursion from 1 to 9, take current number and not take current number
        def dfs(i, nums):
            if i > 9 or len(nums) == k:
                if sum(nums) == n and len(nums) == k:
                    ans.append(nums)
            else:
		# not take
                dfs(i+1, nums.copy())
		# take
                nums.append(i)
                dfs(i+1, nums.copy())
        ans = []
        dfs(1, [])
        return ans
