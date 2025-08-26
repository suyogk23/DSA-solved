# solution by @suyogk23 GITHUB
# do binary search of range(1, max element in piles)
# when cant finish at m rate l=m+1 else, r=m
# this will effectively fing min req k when l == r
#can finish function can be made y finging if sum of ceil(current pile/ current k) >= h,
#finds rate of eating is fast enough to finish the pile
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles = sorted(piles)
        l, r = 1, piles[n-1]
        def canFinish(k):
            hrs = sum(math.ceil(pile/k) for pile in piles)
            return hrs <= h

        while l < r:
            m = (l+r) // 2
            if canFinish(m):
                r = m
            else:
                l = m+1
        
        return r
