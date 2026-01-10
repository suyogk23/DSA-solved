class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        parent = [-1 for _ in range(n)]

        def findParent(node):
            while parent[node] >= 0:
                node = parent[node]
            return node

        for u, v in edges:
            # find parent nodes
            pu = findParent(u)
            pv = findParent(v)
            # union by rank
            if pu != pv: 
                if parent[pu] <= parent[pv]:
                    parent[pu] += parent[pv]
                    parent[pv] = pu
                else:
                    parent[pv] += parent[pu]
                    parent[pu] = pv
        
        connected_components = 0
        for rank in parent:
            if rank < 0:
                connected_components += 1

        return connected_components    
