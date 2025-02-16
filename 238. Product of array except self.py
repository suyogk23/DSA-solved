class Solution:
    # calculate prefix and  suffix product array and use formula: pre[i-1] * suf[i+1]
    # to get the desired result arr
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums
        pre = [0]*n
        pre[0] = nums[0]
        #calculate prefix arr
        for i in range(1,n):
            pre[i] = nums[i]*pre[i-1]
        #calculate suffix arr
        suf = [0]*n
        suf[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            suf[j] = nums[j]*suf[j+1]
        #calculate product: pre[i-1] * suf[i+1]
        ans = [0]*n
        ans[0] = suf[1]
        ans[n-1] = pre[n-2]
        for i in range(1,n-1):
            ans[i] = pre[i-1] * suf[i+1]
        return ans

            

        



        
