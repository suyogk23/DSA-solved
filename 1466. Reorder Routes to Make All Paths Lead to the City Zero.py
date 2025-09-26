class Solution:
    # soultion by @suyogk23 GITHUB
    # maintain 2 adj_list one for dir original edges and other for undirected edges
    # traverse using undirected edges, if neighbour in original adj list and neighbour is not alreay visisted
    # add +1 to ans
    # else continue traversal to unvisited nodes on the undirected graph
    # this solution works on cyclic graph also
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dir_adj_list = defaultdict(list)
        undir_adj_list = defaultdict(list)
        for v, u in connections:
            dir_adj_list[v].append(u)
            undir_adj_list[v].append(u)
            undir_adj_list[u].append(v)
        
        vis = set()
        ans = 0
        def dfs(node):
            nonlocal ans
            vis.add(node)
            for neighbour in undir_adj_list[node]:
                if neighbour in dir_adj_list[node] and neighbour not in vis:
                    ans += 1
                if neighbour not in vis:
                    dfs(neighbour)

        dfs(0)
        return ans

            
        
        
