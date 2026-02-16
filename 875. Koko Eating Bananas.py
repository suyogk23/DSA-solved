from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time: O(n * log (max))
        n = len(piles)
        if h < n: # its not possible to eat bananas faster than n (array size rate)
            return -1

        def getEatTime(rate):
            time = 0
            for pile in piles:
                time += ceil(pile/rate)
            return time
        
        l = 1
        r = max(piles)

        while l < r:
            m = (l+r)//2
            time = getEatTime(m)
            # print(l, r, m, time)
            if time > h:
                # increase rate of eating
                l = m + 1
            else:
                # if time < h, we have to find min rate
                r = m

        return r


        # piles: [3, 5, 2, 1, 10]
        # h: 4
        # k: varies each hour
