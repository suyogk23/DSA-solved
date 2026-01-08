class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # BOTTOM UP
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

        # TOP DOWN
        # dp = [[0 for _ in range(m)] for _ in range(n)]
        # def dfs(i, j):
        #     if i == n or j == m:
        #         return 0
        #     if dp[i][j] is not None:
        #         return dp[i][j]
        #     if text1[i] == text2[j]:
        #         res = 1 + dfs(i+1, j+1)
        #     else:
        #         res = max(dfs(i+1, j), dfs(i, j+1))
        #     dp[i][j] = res
        #     return dp[i][j]

        # return dfs(0, 0)
            

