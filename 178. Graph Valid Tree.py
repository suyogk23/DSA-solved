class Solution:
    # check for tree conditions:
    # 1. no loops
    # 2. no isolated nodes(island)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0 or n == None:
            return True
        #init adj list
        adj_list = {i:[] for i in range(n)}
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        vis = set()
        #dfs to detect loops
        def dfs(node, prev):
            if (node in vis):
                return False
            vis.add(node)
            for nbr in adj_list[node]: 
                if nbr != prev:
                    if not dfs(nbr, node):
                        return False

            return True
        #check for loops and island nodes
        
        if (not dfs(0, -1)) or (len(vis) != n):
            print(len(vis))
            return False

        return True
            
        
        
