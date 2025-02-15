class Solution:
    #suproblem: 
    '''
    1. check while taking current digit as a single digit (if cur dig != 0)
    2. check while including current digit and next difit as 2 digits (if cur dig <2 and
    next digit <= 6)
    '''
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp = {n:1}

        def f(i):
            if (i in dp):
                return dp[i]
            if (s[i] == "0"):
                return 0

            res = f(i+1)
            if i+1 < n:
                    #first digit = (1 or 2) #second digit <= 6
                if s[i]=='1' or s[i]=='2' and s[i+1] in "0123456":
                    res += f(i+2)
            dp[i] = res
            return res
        
        return f(0)
        

            

