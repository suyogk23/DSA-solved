class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        def checkPal(l, r):
            nonlocal res
            while (l>=0 and r<n) and s[l]==s[r]:
                #if pallindrome increase count
                res+=1
                l-=1
                r+=1
                
        for i in range(n):
            #odd pallindromes
            checkPal(i, i)
            #even pallindromes
            checkPal(i, i+1)
            
        return res
                    


                    
        
