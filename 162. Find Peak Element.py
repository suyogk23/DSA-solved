class Solution:
    # solution by @suyogk23 GITHUB
    # do bin search, if cur idx element is peak return idx
    # else: check if left ele is greater, then shift r to idx-1 else f next ele is greater shift l to idx+1
    # continue binary search
    # to cover edge cases append -inf to first and last pos of the array
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        n = len(nums)
        l, r = 1, n-2
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid-1] > nums[mid]:
                r = mid-1
            elif nums[mid+1] > nums[mid]:
                l = mid+1
            else:
                return mid-1
