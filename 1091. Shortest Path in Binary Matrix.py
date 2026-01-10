class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # do BFS if u encounter i, j = n-1, n-1 then u immediately return on the first encounter
        if grid[0][0] == 1:
            return -1
        rvec = [-1, 0, 0, 1, 1, -1, 1, -1]
        cvec = [0, 1, -1, 0, 1, -1, -1, 1]
        n = len(grid)
        vis = [[False for _ in range(n)]for _ in range(n)]
        q = deque([(0, 0)])
        shortest_path = 1

        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                front = q.popleft()
                i, j = front[0], front[1]
                if i==(n-1) and j==(n-1):
                    return shortest_path
                for v in range(8):
                    r = i + rvec[v]
                    c = j + cvec[v]
                    if r>=0 and c>=0 and r<n and c<n and grid[r][c]==0 and not vis[r][c]:
                        vis[r][c] = True
                        q.append((r, c))
            shortest_path += 1
            
        return -1
