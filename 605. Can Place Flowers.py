class Solution:
    # solution by @suyogk23
    # do a linear pass and check prev and next index has 0 as element, if yes then make it 1 and reduce n by 1
    # make sure to handle edge cases
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if n == 0:
            return True
        if l == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            return False

        for i in range(l):
            prev_idx, next_idx = i-1, i+1
            if flowerbed[i] == 0:
                # edge cases
                if i == 0 and next_idx < l:
                    if flowerbed[next_idx] == 0:
                        n -= 1
                        flowerbed[i] = 1
                elif i == l-1 and prev_idx >= 0:
                    if flowerbed[prev_idx] == 0:
                        n -= 1
                        flowerbed[i] = 1
                # main case
                else:
                    if flowerbed[prev_idx] == 0 and flowerbed[next_idx] == 0:
                        n -= 1
                        flowerbed[i] = 1
        if n <= 0:
            return True
        return False


                
        
