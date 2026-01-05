class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up (tabulation)
        if n == 1:
            return 1
        
        c1, c2 = 1, 2

        for i in range(n-2):
            temp = c2
            c2 = c1+c2
            c1 = temp
        return c2
