class Solution:
    # solution by @suyogk23 GITHUB
    # 3 possibilities: buy, sell or hold stock
    # refer code for logic
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, holding):
            if i >= n:
                # base case
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            # not take
            profit = dfs(i+1, holding)

            #take
            # profit = sell_price - buy_price - fee
            if not holding:
                # buy
                profit = max(profit, dfs(i+1, 1) - prices[i])
            else:
                # sell: this value will eventually be returned to the call that belongs to buy
                profit = max(profit, prices[i] + dfs(i+1, 0) - fee)
            
            dp[(i, holding)] = profit
            return profit

        return dfs(0, 0)


