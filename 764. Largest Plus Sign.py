class Solution:
    # solution by @suyogk23 GITHUB
    '''
    Construct the grid with 1s and make all the mines indices equal to 0
    Find the prefix sum matrix for top and left for each element in grid
    Find the postfix sum matrix for bottom and right for each element in grid
    for each index in grid find he minimum of left, right, top, bottom values (intutively this will be the size of the largest +)
    '''
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # build a grid
        grid = [[1]*n for i in range(n)]
        for i in mines:
            x, y = i[0], i[1]
            grid[x][y] = 0

        left = [[0]*n for i in range(n)]
        right = [[0]*n for i in range(n)]
        top = [[0]*n for i in range(n)]
        bottom = [[0]*n for i in range(n)]
        # left and top
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    #left
                    if j == 0:
                        left[i][j] = 1
                    else:
                        left[i][j] = left[i][j-1] + 1
                    #top
                    if i == 0:
                        top[i][j] = 1
                    else:
                        top[i][j] = top[i-1][j] + 1
        # right and bottom
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    #right
                    if j == n-1:
                        right[i][j]=1
                    else:
                        right[i][j] = right[i][j+1]+1
                    #bottom
                    if i == n-1:
                        bottom[i][j]=1
                    else:
                        bottom[i][j] = bottom[i+1][j]+1
        # find the biggest + 
        max_plus = 0
        for i in range(n):
            for j in range(n):
                max_plus = max(max_plus, min(min(left[i][j],right[i][j]), min(top[i][j], bottom[i][j])))
        
        return max_plus
                

        
                        


        
