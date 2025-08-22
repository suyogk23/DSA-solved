class Solution:
    # solution by @suyogk23 GITHUB
    # do bfs while counting steps
    # when on edge row or col return strps
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        # use '+' to mark as visited
        q = deque([entrance+[0]])
        maze[entrance[0]][entrance[1]] = '+'

        row_vec = [1,0,0,-1]
        col_vec = [0,-1,1,0]

        while q:
            node = q.popleft()
            for i in range(4):
                row = node[0] + row_vec[i]
                col = node[1] + col_vec[i]
                steps = node[2]
                if row < m and col < n and row >= 0 and col >= 0:
                    if maze[row][col] == '.':
                        if row == m-1 or col == n-1 or row == 0 or col == 0:
                            # print(row, col)
                            return steps + 1
                        else:
                            q.append([row, col, steps+1])
                            maze[row][col] = '+'
                            # print(q)
        
        return -1

        
        
