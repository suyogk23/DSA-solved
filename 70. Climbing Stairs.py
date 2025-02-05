class Solution:
    #DP: all approaches
    def climbStairs(self, n: int) -> int:
        #bottom up
        # arr = [-1 for i in range(n+1)]
        # def top_down(n):
        #     #base cases
        #     if n==0:
        #         return 1
        #     if(arr[n]==-1):
        #         if n>=2:
        #             arr[n] = top_down(n-2) + top_down(n-1)
        #             return arr[n]
        #         else:
        #             arr[n] = top_down(n-1)
        #             return arr[n]
        #     else:
        #         return arr[n]
        
        # top_down(n)
        # return arr[n]

        #top down
        # arr = [0 for i in range(n+1)]
        # if n<=2:
        #     return n
        # arr[1], arr[2] = 1, 2
        # for i in range (3, n+1):
        #     arr[i] = arr[i-1]+arr[i-2]
        # return arr[n]

        #space optimised
        if n<=2:
            return n
        temp = 0
        prev = 1
        cur = 2
        for i in range(3, n+1):
            temp = cur
            cur = cur+prev
            prev = temp
        return cur


        