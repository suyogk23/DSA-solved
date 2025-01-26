class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if there is a cycle then the courses can NOT be completed
        adjList = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            adjList[i].append(j)
        
        vis = set()
        for i in range(numCourses):
            if not self.dfs(i, adjList, vis):
                return False
        
        return True
    
    def dfs(self, i, adjList, vis):
        if(i in vis):
            return False
        vis.add(i)
        for j in adjList[i]:
            res = self.dfs(j, adjList, vis)
            if not res:
                return False
        adjList[i] = []
        vis.remove(i)
        return True
        

        

        
            
        


        
