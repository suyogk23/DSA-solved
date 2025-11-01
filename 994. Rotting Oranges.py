class Solution:
    # solution by @suyogk23 GITHUB
    # do bfs and track min time in m x n time array and rotten orange source could be multiple
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # global constants
        m, n = len(grid), len(grid[0])
        rvec = [0, -1, 1, 0]
        cvec = [-1, 0, 0, 1]
        # rot time information to keep track of min time from multiple source
        rot_time = [[float('inf') for _ in range(n)] for _ in range(m)]
        # bfs traversal and time updation
        def bfs(x, y):
            vis = set()
            q = deque([(x, y, 0)])
            while q:
                #check nodes each level
                for i in range(len(q)):
                    node = q.popleft()
                    row = node[0]
                    col = node[1]
                    time = node[2]
                    rot_time[row][col] = min(rot_time[row][col], time)
                    vis.add((row, col))
                    for i in range(4):
                        r = row + rvec[i]
                        c = col + cvec[i]
                        if r>=0 and c>=0 and r<m and c<n:
                            if ((r, c) not in vis) and (grid[r][c] == 1):
                                # update rot time to minimum
                                q.append((r, c, time+1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs(i, j)
        # check for isolated fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and rot_time[i][j] == float('inf'):
                    return -1
        # check for max rot time
        max_rot_time = 0
        for i in range(m):
            for j in range(n):
                if rot_time[i][j] != float('inf'):
                    max_rot_time = max(max_rot_time, rot_time[i][j])
        return max_rot_time



        
