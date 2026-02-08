class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # TC: O(n)
        # Space: constant
        n = len(nums)
        pos = neg = ans = 0
        # we track the len of longest pos and neg subarray length
        # if we encounter a negative product we will decrement subarray length, assign pos to the len of subarray from cur idx until prev neg idx
        # if the product s pos we will assign pos to the subarr length
        for i in range(n):
            if nums[i] == 0:
                pos = neg = 0
            if nums[i] < 0: # negative num
                temp = pos
                pos = (neg + 1) if neg > 0 else 0
                neg = temp + 1
            if nums[i] > 0: # positive num
                pos += 1
                neg = (1 + neg) if neg > 0 else 0
            print(pos)
            ans = max(ans, pos)

        return ans
