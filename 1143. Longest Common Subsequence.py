class Solution:
    # solution by @suyogk GITHUB
    # if text1[i] == text2[j]: DP[i][j] = DP[i + 1][j + 1] + 1 
    # else: DP[i][j] = max(DP[i + 1][j], DP[i][j + 1])
    # handle base case 
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = {}
        def dfs(i, j):
            if i >= n1 or j >= n2:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                dp[(i, j)] =  1 + dfs(i+1, j+1)
                return dp[(i, j)]
            else:
                dp[(i, j)] = max(dfs(i, j+1), dfs(i+1, j))
                return dp[(i, j)]
        
        return dfs(0, 0)
