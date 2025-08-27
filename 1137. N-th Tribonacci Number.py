class Solution:
    # solution b @suyogk23 GITHUB
    # extentions of normal fib
    # maintain 3 prev variables and swap them accordingly 
    def tribonacci(self, n: int) -> int:
        if n < 3:
            if n == 0:
                return 0
            else:
                return 1

        prev1 = 0
        prev2 = 1
        prev3 = 1
        for i in range(3, n+1):
            cur = prev1 + prev2 + prev3
            prev1, prev2 = prev2, prev3
            prev3 = cur
            
        return prev3
