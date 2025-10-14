class Solution:
	# find max element in array
	# if current element is greater than or equal to max element, append
	# true in output array, else append false
	# solution by @suyogk23 GITHUB 
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
