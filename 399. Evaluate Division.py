class Solution:
    # for each equantion, consider elements as node and weigted edges as values[i] or 1/values[i]
    # a/b create a node a --(values[i])--> b and b--(1/values[i])-->a
    # now traverse the graph with source = query[0] and destination = query[1] 
    # find the product of the path from source to destination
    # return this product if the query is valid, else return -1
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        for i, equation in enumerate(equations):
            adj_list[equation[0]].append((equation[1], values[i]))
            adj_list[equation[1]].append((equation[0], 1/values[i]))
        
        def calculate(source, destination):
            if source not in adj_list or destination not in adj_list:
                return -1.0
            vis = set()
            def dfs(node, path=1):
                if node == destination:
                    return path
                vis.add(node)
                for neighbour, edge in adj_list[node]:
                    # print(node, adj_list[node])
                    if neighbour not in vis:
                        found = dfs(neighbour, path*edge)
                        if found is not None:
                            return found
                return None
            result = dfs(source)
            if result:
                return result
            else:
                return -1.0

        ans = []
        for start, end in queries:
            ans.append(calculate(start, end))
       
        return ans

