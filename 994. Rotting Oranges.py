class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS 
        n, m = len(grid), len(grid[0])
        rvec, cvec = [-1, 0, 0, 1], [0, -1, 1, 0]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        # add all rotten oranges as starting source to Q
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2 and vis[i][j] == 0:
                    # ans += rot(i, j)
                    q.append((i, j))
        # Simulate rotting process, do BFS traversal from the source
        duration = -1
        while q:
            cur_q_len = len(q)
            for i in range(cur_q_len):
                node = q.popleft()
                for v in range(4):
                    r = node[0] + rvec[v]
                    c = node[1] + cvec[v]
                    # if there is an orage adj then rot it and mark as visited
                    if r>=0 and c>=0 and r<n and c<m and grid[r][c]==1:
                        if vis[r][c] == 0:
                            vis[r][c] = 1
                            grid[r][c] = 2
                            q.append((r, c)) 
            duration += 1
        # check for any unrotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return duration if duration > 0 else 0
