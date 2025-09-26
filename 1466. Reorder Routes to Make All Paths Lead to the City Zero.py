class Solution:
    # solution by @suyogk23 GITHUB
    # this solution only works for acyclic graphs (trees)
    # maintain an undir duplicate edge with sign 0 and original directed edge with sign 1
    # traverse the tree in dfs, only go to neighbour if the neighbour is != parent (remember the graph is acyclic thats why this works)
    # maintain a global ans var and add sign to it (+1 if original edge else 0), this automatically tracks the edges to flip
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in connections:
            adj_list[u].append([v, 1]) # sign = 1, for original directed edge
            adj_list[v].append([u, 0]) # sign = 0, for undirected edge

        ans = 0
        def dfs(parent, node):
            nonlocal ans
            for neighbour, sign in adj_list[node]:
                if neighbour != parent:
                    ans += sign
                    dfs(node, neighbour)
        
        dfs(-1, 0)
        return ans
        
