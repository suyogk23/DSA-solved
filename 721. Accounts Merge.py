class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        # THE CONNECTED COMPONENTS INFO WILL BE STARED IN uf.parent, do not worry onmap level on connected components
        # create mappings from {email -> index} and apply union find on them
        # connect related components using union find
        eiMap = {}
        for i, acc in enumerate(accounts):
            for a in acc[1:]:
                if a in eiMap:
                    uf.union(i, eiMap[a])
                else:
                    eiMap[a] = i
        # aggregate the emails based on connected components
        eiGroup = defaultdict(list)
        for e, i in eiMap.items():
            root_user = uf.findParent(i) # root_user is parent of the connected components
            eiGroup[root_user].append(e)
        # prepare final answer with name + sorted emails
        merged_accounts = []
        for i, e_group in eiGroup.items():
            name = accounts[i][0]
            e_group.sort()
            merged_accounts.append([name]+e_group)

        return merged_accounts

class UnionFind:
    parent = []
    def __init__(self, n=0):
        self.parent = [-1 for _ in range(n)]
    
    def findParent(self, node):
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu != pv:
            if self.parent[pu] <= self.parent[pv]:
                self.parent[pu] += self.parent[pv]
                self.parent[pv] = pu
            else:
                self.parent[pv] += self.parent[pu]
                self.parent[pu] = pv
            
