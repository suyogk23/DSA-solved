# soultion by @suyogk23 GITHUB
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k != 0:
            return False

        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        max_duplicate_allowed = n // k
        for val in d.values():
            if val > max_duplicate_allowed:
                return False
        return True
