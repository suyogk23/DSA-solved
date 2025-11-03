class Solution:
    # solution by @suyogk23 GITHUB
    # maintain 2 ptrs to s and t,
    # if s[sp] == t[tp]: sp+=1
    # tp+=1
    # if sp == len(s) return true
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        sp, tp = 0, 0

        while sp < n and tp < m:
            if s[sp] == t[tp]:
                sp += 1   
            tp+=1
        
        if sp == n:
            return True
        
        return False

        
