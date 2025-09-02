class Solution:
    # Solution by @suyogk23 GITHUB
    # recurse to down(row + 1) + right (col + 1)
    # when row = m and col = n return 1
    # handle base case
    # use dp to speed up process
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(row, col):
            if row > m or col > n:
                return 0
            if row == m and col == n:
                return 1
            if (row, col) in dp:
                return dp[(row, col)]
            dp[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
            return dp[(row, col)]

        return dfs(1, 1)
