class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # TC: O(n)
        global_max = nums[0] # global max subarray sum
        local_max = nums[0] # max subarray sum until nums[i]

        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            global_max = max(global_max, local_max)

        return global_max

