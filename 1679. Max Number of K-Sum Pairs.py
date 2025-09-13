class Solution:
    # soluton by @suyogk23 GITHUB
    # sort the array
    # l and r ptr at opposite ends
    # if sum of l + r < k then l moves left (smallest num + larget num is still lesser than k)
    # else r moves right 
    # if equal increase operation count
    def maxOperations(self, nums: List[int], k: int) -> int:
        l , r = 0, len(nums)-1
        ans = 0
        nums.sort()
        
        while l < r:
            s = nums[l] + nums[r]
            if  s == k:
                ans += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1

        return ans
