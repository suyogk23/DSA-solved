class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        max_len = 0
        
        def checkPal(l, r):
            nonlocal res, max_len
            while (l>=0 and r<n) and s[l]==s[r]:
                # update res if cur len greater than max len palindrome
                cur_len = r-l+1
                if cur_len > max_len:
                    res = s[l:r+1]
                    max_len = cur_len
                l-=1
                r+=1
                
        for i in range(n):
            #odd pallindromes
            checkPal(i, i)
            #even pallindromes
            checkPal(i, i+1)
            
        return res
                    

                    
        

