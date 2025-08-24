# solution by @suyogk23 GITHUB
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n == 1:
            return 1
        sumOdd = 0
        sumEven = 0
        for i in range(1, n*2+1):
            if i%2 == 0:
                #even
                sumEven += i
            else:
                #odd
                sumOdd += i
        return math.gcd(sumOdd, sumEven)
            

                
        
