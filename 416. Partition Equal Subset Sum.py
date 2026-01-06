class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            # odd num total cant have array divided exactly by 2 equal sum subsets
            return False
        target = total//2
        # bottom up using a set, the set building imitates take and not take for subset sum
        dp = {0}
        for num in nums:
            next_dp = set()
            for ele in dp:
                next_dp.add(ele+num)
                next_dp.add(ele)
            if target in next_dp:
                return True
            dp = next_dp
        return False
            

