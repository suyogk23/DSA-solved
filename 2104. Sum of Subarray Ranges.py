class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # find sum of minimum values in subarray - sum of maximum values in subarray
        n = len(nums)
        nse, psee, nge, pgee = [0]*n, [0]*n, [0]*n, [0]*n
        seStk, geStk = [], []
        for i in range(n-1, -1, -1):
            #next smaller element
            while seStk and nums[seStk[-1]] >= nums[i]:
                seStk.pop()
            if not seStk:
                nse[i] = n
            else:
                nse[i] = seStk[-1]
            seStk.append(i)
            # next greater than element
            while geStk and nums[geStk[-1]] <= nums[i]:
                geStk.pop()
            if not geStk:
                nge[i] = n
            else:
                nge[i] = geStk[-1]
            geStk.append(i)

        seStk, geStk = [], []
        for i in range(n):
            # prev smaller or equal to element
            while seStk and nums[seStk[-1]] > nums[i]:
                seStk.pop()
            if not seStk:
                psee[i] = -1
            else:
                psee[i] = seStk[-1]
            seStk.append(i)
            # prev greater than or equal to element
            while geStk and nums[geStk[-1]] < nums[i]:
                geStk.pop()
            if not geStk:
                pgee[i] = -1
            else:
                pgee[i] = geStk[-1]
            geStk.append(i)

        # summation
        # summation of minimum in subarrays and maximum in subarrays
        min_summation = 0
        max_summation = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            min_summation += (left * right * nums[i])
        # summation of maximum in subarrays
        for i in range(n):
            left = i - pgee[i]
            right = nge[i] - i
            max_summation += (left * right * nums[i])

        ans = max_summation - min_summation
        return ans
        
