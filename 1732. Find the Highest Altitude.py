class Solution:
    # iterate and calculate largets prefixSum
    # return max(0 or prefixSum)
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        prefixSum = 0
        for i in range(len(gain)):
            prefixSum += gain[i]
            max_h = max(max_h, prefixSum)
        return max_h

