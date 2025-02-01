from typing import Set
class Solution:
    '''
        this is a graph problem: dfs cycle detection or topological sort, 
        if cycle exists, all course can not be completed, 
        else all courses can be completed
        - build adj list
        - make a visit and cycle(to check cycles) set
            - dfs and check for cycles, before dfs function ends keep appending to ans_list,
            add node to vis and remove node from cycle
        - if cycle return []
        - else return ans_list
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #build adj list
        adj_list = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            adj_list[i[0]].append(i[1])
        #make visit set
        vis, cycle = set(), set()
        ans_list = []
        for j in range(len(adj_list)):
            if not self.dfs(j, adj_list, vis, cycle, ans_list):
                return []

        return ans_list

    def dfs(self, node:int, adj_list:List[List[int]], vis:Set[int], cycle:Set[int], ans:List[int])->bool:
        #base cases
        #1. check cycle: 
        if node in cycle:
            return False
        if node in vis:
            return True
        cycle.add(node)
        for i in adj_list[node]:
            res = self.dfs(i, adj_list, vis, cycle, ans)
            if not res:
                return False
        cycle.remove(node)
        vis.add(node)
        ans.append(node)
        return True
        
        
