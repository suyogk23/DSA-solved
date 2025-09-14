class Solution:
    # solution by @suyogk23 GITHUB
    # idea: use prefix (leftSum) and postfix (rightSum)
    # at index i: exclude nums[i] from both sides
    # check if leftSum == rightSum → pivot found
    # edge cases: start (leftSum=0) or end (rightSum=0)
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
