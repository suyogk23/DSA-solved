class Solution:
    # bottom up
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(1,amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin]
    
        return dp[amount]

    # top down
    '''
    class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        def dfs(i, target):
            if i >= n and target != 0:
                return 0
            if target == 0:
                return 1
            if (i, target) in dp:
                return dp[(i, target)]
            take = 0
            if coins[i] <= target:
                take = dfs(i, target-coins[i])
            not_take = dfs(i+1, target)
            dp[(i, target)] = take + not_take
            return dp[(i, target)]
        
        return dfs(0, amount)
        
    ''' 
