class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # TC: O(n^2), (n) * (n-1) * (n-2) .... = n(n-1)/2
        # Space: O(n)
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums)-1):
                new_nums.append((nums[i] + nums[i+1]) % 10)
            nums = new_nums

        return nums[0]
