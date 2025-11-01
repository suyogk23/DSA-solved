class Solution:
    # solution by @suyogk23 GITHUB
    # keep track of number of fresh oranges
    # now append all rotten source in tree and do bfs
    # if fresh oranges are left after bfs then return -1
    # else return the time elapsed (number of levels in bfs -> track this in queue)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # global constants
        m, n = len(grid), len(grid[0])
        rvec = [0, -1, 1, 0]
        cvec = [-1, 0, 0, 1]
        q = deque()
        # keep track of fresh orange count in array
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
        # append all the rotten sources in the queue, this way, we can simulate multi source rot from BFS traversal
        # all sources will have time = 0 initially
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, time))
        while q:
            #check nodes each level
            for i in range(len(q)):
                node = q.popleft()
                row, col , time = node[0], node[1], node[2]
                for i in range(4):
                    r = row + rvec[i]
                    c = col + cvec[i]
                    if r>=0 and c>=0 and r<m and c<n:
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            fresh -= 1 # this is required to check if it is possible to rot all oranges(no fresh isolated oranges)
                            q.append((r, c, time + 1))
        if fresh > 0:
            return -1 # not possible to rot all oranges
            
        return time
                    



        

