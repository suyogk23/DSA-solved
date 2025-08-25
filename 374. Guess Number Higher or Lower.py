# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# solution by @suyogk23 GITHUB
# implement a simple binary search
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = (l+r)/2
            res = guess(m)
            if res == 0:
                return int(m)
            elif res == -1:
                # target is lower than m
                r = m
            else:
                #target is higher than m
                l = m



            
        
