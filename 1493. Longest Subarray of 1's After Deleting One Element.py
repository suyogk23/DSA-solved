class Solution:
    # solution by @suyogk23 GITHUB
    # expand the slididng window from right while the count of zeroes is less than 1
    # if the count of zeros is greater than 1 contract the sliding window from left
    # maintain the max of cur_len and max_len
    # the above operations must be done in the exact same sequence
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        zero_count = 0
        max_len = 0
        while r < n:
            if nums[r] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            r += 1
            max_len = max(max_len, r-l-1)
        
        return max_len
