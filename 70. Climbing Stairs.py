class Solution:
    #dp: optimized approach
    def climbStairs(self, n: int) -> int:
        arr = [-1 for i in range(n+1)]

        def dp(n):
            #base cases
            if n==0:
                return 1
            if(arr[n]==-1):
                if n>=2:
                    arr[n] = dp(n-2) + dp(n-1)
                    return arr[n]
                else:
                    arr[n] = dp(n-1)
                    return arr[n]
            else:
                return arr[n]
        
        dp(n)
        return arr[n]
        
