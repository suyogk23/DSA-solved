class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def findParent(node):
            if node != parent[node]:
                parent[node] = findParent(parent[node])
            return parent[node]

        def union(u, v):
            parent_u, parent_v = findParent(u), findParent(v)
            if parent_u == parent_v:
                return False
            if rank[parent_u] >= rank[parent_v]:
                rank[parent_u] += rank[parent_v]
                parent[parent_v] = parent_u
            else:
                rank[parent_v] += rank[parent_u]
                parent[parent_u] = parent_v
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u,v]

            

