class Solution:
    # the input is literally an adj list
    # grapthify the problem and solve it
    # solution by @suyogk23 GITHUB
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        if n <= 1:
            return True
        vis = [0]*n

        def dfs(node):
            if vis[node]:
                return
            vis[node] = 1
            for neighbour in rooms[node]:
                dfs(neighbour)
        
        dfs(0)

        for i in vis:
            if i == 0:
                return False
        return True
        
