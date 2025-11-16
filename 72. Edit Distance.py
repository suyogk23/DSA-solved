class Solution:
    # solution by @suyogk23 GITHUB
    # for each idx check all 3 operations (insert, delete and replace)
    # replace = 1 + dfs(p1+1, p2+1) 
    # delete = 1 + dfs(p1+1, p2)
    # insert = 1 + dfs(p1, p2+1)
    # memoize this and pay attention to base cases 
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = {}
        #return int
        def dfs(p1, p2):
            if (p1, p2) in dp:
                return dp[(p1, p2)]
            # base cases
            if p1 == n1:
                return n2-p2 # remaining inserts
            if p2 == n2:
                return n1-p1 # remaining deletions
            # skip
            if word1[p1] == word2[p2]:
                dp[(p1, p2)] = 0 + dfs(p1+1, p2+1)
                return dp[(p1, p2)]
            replace, delete, insert = float('inf'), float('inf'), float('inf')
            # replace
            replace = 1 + dfs(p1+1, p2+1)
            # delete
            delete = 1 + dfs(p1+1, p2)
            # insert
            insert = 1 + dfs(p1, p2+1)
            # store min
            dp[(p1, p2)] = min(insert, replace, delete)
            return dp[(p1, p2)]
        return dfs(0, 0)
        



            

        
