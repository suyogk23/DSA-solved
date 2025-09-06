class Solution:
    # solution by @suyogk23 GITHUB
    # in XOR operation if we xor two same numbers the result will be 0
    # hence if we xor each and every number in the list the non duplicate will be the
    # final XOR result
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor = xor ^ nums[i]
        return xor
        
