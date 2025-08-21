'''
solution by @suyogk23 GITHUB
Create a vis array of size len(input)
for each unvisited node do dfs or bfs:
    do province +=1
The intution is if we do a dfs/bfs on unvisisted node it will visit all connected nodes and mark them as visited
Hence the iteration on vis array will account for provinces as it will do bfs/dfs on each connected set of nodes/provinces
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0]*n

        def dfs(node):
            vis[node] = 1
            for neighbour in range(n):
                if isConnected[node][neighbour]:
                    if not vis[neighbour]:
                        dfs(neighbour)
        
        provinces = 0
        for node in range(len(vis)):
            if not vis[node]:
                dfs(node)
                provinces+=1

        return provinces
                        
