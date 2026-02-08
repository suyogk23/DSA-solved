class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # TC: O(n), amotized
        # Space: O(n)

        #idea: if we calcuate every element's occurance as the minimum element in the subarray, 
        # we can calculate the sum of minimums in all the subarrays
        # we find the limits of the sub array in whih the cur element is smallst, towards left and right
        # we then find all combinations of subarry with above condition and multiply it with the ele
        # we then add it to the answer
        n = len(arr)
        
        def getNextSmallerElement():
            ans = [-1] * n
            stk = []
            for i in range(n-1, -1, -1):
                while stk and arr[stk[-1]] >= arr[i]:
                    stk.pop()
                if not stk:
                    ans[i] = n
                else:
                    ans[i] = stk[-1]
                stk.append(i)
            return ans
        
        def getprevSmallerOrEqualElement(): # beacuse each duplicate element must be calculated exatly once when equal elements are present
            ans = [-1] * n
            stk = []
            for i in range(0, n):
                while stk and arr[stk[-1]] > arr[i]:
                    stk.pop()
                if not stk:
                    ans[i] = -1
                else:
                    ans[i] = stk[-1]
                stk.append(i)
            return ans
        
        nse = getNextSmallerElement()
        psee = getprevSmallerOrEqualElement()
 
        ans = 0
        MOD = 10**9 + 7
        for i in range(n):
            left_bounds = i-psee[i]
            right_bounds = nse[i]-i
            ans += ((arr[i] * left_bounds * right_bounds)%MOD)
        return ans % MOD
