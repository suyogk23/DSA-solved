class Solution {
    int rv[4] = {0,1,-1,0};
    int cv[4] = {1,0,0,-1};

    void dfs(int r, int c, vector<vector<char>>& grid, vector<vector<int>>& vis){
        vis[r][c] = 1;
        for(int i=0; i<4; i++){
            int row=r+rv[i], col=c+cv[i];
            if(row<grid.size() && col<grid[0].size() && row>=0 && col>=0){
                if(grid[row][col]=='1' && vis[row][col]==0){
                    dfs(row, col, grid, vis);
                }
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<int>> vis(grid.size(), vector<int>(grid[0].size(), 0));
        int ans = 0;
        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
                if(grid[i][j]=='1' && vis[i][j]==0){
                    dfs(i,j,grid,vis);
                    ans++;
                }
            }
        }
        return ans;
    }
};
