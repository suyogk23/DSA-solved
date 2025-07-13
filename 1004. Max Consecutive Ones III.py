class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r, count_0, max_l = 0, 0, 0, 0
        while (r < n):
            if (nums[r] == 0):
                count_0+=1
            while(l <= r and count_0 > k):
                if (nums[l] == 0):
                    count_0-=1
                l+=1
            max_l = max(max_l, r-l+1)
            r+=1
        return max_l
            
