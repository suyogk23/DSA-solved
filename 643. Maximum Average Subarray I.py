# solution by @suyogk23 GITHUB
# simple sliding window, slide over the array from left to right with window size k until right reaches end of array

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        l, r = 0, k-1
        cur_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_avg = cur_sum / k

        while (r < n-1):
            cur_sum -= nums[l]
            l += 1
            r += 1
            cur_sum += nums[r]
            cur_avg = cur_sum / k
            max_avg = max(max_avg, cur_avg)
        
        return max_avg


            
