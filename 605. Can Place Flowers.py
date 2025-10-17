class Solution:
    # solution by @suyogk23 GITHUB
    # prepend and append 0 at first and last index
    # now do a linear pass of array and check if [i-1] + [i] + [i+1] elements sum to 0
    # if yes then decrease n by 1, and make flowerbed[idx] = 1
    # finally after iteration return true is n<=0 else return false
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        for i in range(1, len(flowerbed)-1):
            if (flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]) == 0:
                n -= 1
                flowerbed[i] = 1
        
        if n <= 0:
            return True
        return False


                
        
