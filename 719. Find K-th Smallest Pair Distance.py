class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Time: O(n log n + n log max)
        # Space:: O(1)
        n = len(nums)
        nums.sort() # n log n
        # helper to get num of differences less than a num(diff): sliding window on sorted array = max abs difference
        # ensure max abs difference is always <= diff(function argument)
        # after that the diff in right-left index gives us num of pairs with difference <= diff
        # continue the process for the entire array and accumulate the num of pairs count, return the pair count value 
        def getLessThanCount(diff): #O(n)
            left = 0
            count = 0
            for right in range(1,n):
                while left < right and abs(nums[left] - nums[right]) > diff:
                    left += 1
                if left < right:
                    count += (right - left)
            return count

        # binary search to find the kth smallest pair
        r = max(nums)
        l = 0

        while l < r: #O(n log max)
            m = (l+r)//2
            less_than_count = getLessThanCount(m)
            if less_than_count < k:
                l = m + 1
            else:
                r = m

        return r



        
