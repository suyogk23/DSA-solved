class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        # elements with same val will take same num of operations to become 0
        # elements with different val will take different num of oprerations to become 0
        # if we simulate we can see that, the num of operations required will depend on num of non unique elements other than 0
        
        s = set(nums)
        n = len(s)
        if 0 in s:
            return n - 1
        return n


