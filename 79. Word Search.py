class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(word)
        n, m = len(board), len(board[0])
        vis = set()
        rvec = [0, -1, 1, 0]
        cvec = [-1, 0, 0, 1]
        def dfs(r, c, p):
            if p == l-1:
                return True
            vis.add((r, c))
            for i in range(4):
                row = r + rvec[i]
                col = c + cvec[i]
                if row<n and col<m and row>=0 and col>=0:
                    if (row, col) not in vis and board[row][col] == word[p+1]:
                        res = dfs(row, col, p+1)
                        if res:
                            return res
            vis.remove((r, c))
            return False

        for r in range(n):
            for c in range(m):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False

        

                        

