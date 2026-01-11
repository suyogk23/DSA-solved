class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # the course can NOT be completed if there is a cyclic dependencies 

        # adj list
        adj = defaultdict(set)
        for u, v in prerequisites:
                adj[u].add(v)
        # current state of node
        # 0 = unvisited
        # 1 = visiting
        # 2 = visited
        state = [0 for _ in range(numCourses)]

        # track cycles for only current compnenet in graph (if state = 1)
        def dfs(i):
            if state[i] == 1:
                return True # cycle dtetcted
            if state[i] == 2:
                return False

            state[i] = 1
            for n in adj[i]:
                if dfs(n):
                    return True
            state[i] = 2
            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        
