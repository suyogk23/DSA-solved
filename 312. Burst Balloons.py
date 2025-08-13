class Solution:
    '''
    Solution by @suyogk23 GITHUB
    The subproblem is: what is max(coin value if 'i'th element is popped last)
    do this for each element in array, and for itss corresponding right and left subarray
    base case is l > r
    TC: O(n^3)
    SC: O(n^2)
    '''
    def maxCoins(self, nums: List[int]) -> int:
        # add 1 at start and end as per question
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            max_coins = 0
            for i in range(l, r+1):
                coins = (nums[l-1]*nums[i]*nums[r+1])
                #left subarray
                coins += dfs(l, i-1)
                #right subarray
                coins += dfs(i+1, r)
                max_coins = max(max_coins, coins)
            return max_coins

        return dfs(1, len(nums)-2)
