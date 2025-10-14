class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxEle = 0
        for i in candies:
            maxEle = max(maxEle, i)
        ans = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= maxEle:
                ans.append(True)
            else:
                ans.append(False)
        return ans
