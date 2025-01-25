class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        len_row = len(heights)
        len_col = len(heights[0])
        traverse = [(0,1),(1,0),(0,-1),(-1,0)]
        pac_vis, atl_vis = set(), set()

        def dfs(row, col, vis, prevHeight):
            if(row<0 or col<0 or row>=len_row or col>=len_col or (row,col)in vis 
                or heights[row][col]<prevHeight):
                return 
            vis.add((row, col))
            for (r, c) in traverse:
                dfs(row+r, col+c, vis, heights[row][col])
        
        for i in range(len_row):
            #left-pacific
            dfs(i, 0, pac_vis, heights[i][0])
            #right-atlantic
            dfs(i, len_col-1, atl_vis, heights[i][len_col-1])

        for j in range(len_col):
            #top-pacific
            dfs(0, j, pac_vis, heights[0][j])
            #bottom-atlantic
            dfs(len_row-1, j, atl_vis, heights[len_row-1][j])
    
        ans = list()
        for i in range(len_row):
            for j in range(len_col):
                if (i,j) in pac_vis and (i, j) in atl_vis:
                    ans.append([i, j])
    
        return ans



