class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # use 2 ptrs, fix r, when r != l, from s[l:r], find the next element matchng to r
        # swap them to l, note the number of swaps required
        # in odd pal, if u find 1 mid unique character, note its index and move the r ptr to the left

        # this approach ensures relative opposite ordering theory (check leo's solution)
        n = len(s)
        pal = list(s)
        l, r = 0, n-1
        swaps = 0
        centre = -1

        while l < r:
            if pal[l] != pal[r]:
                is_centre = False
                # find the nearest matching element in left part
                for i in range(l, r+1):
                    if i == r:
                        is_centre = True
                        break
                    elif pal[i] == pal[r]:
                        # swap simulation
                        for j in range(i, l, -1):
                            pal[j], pal[j-1] = pal[j-1], pal[j]
                        swaps += (i-l)
                        break
                
                if is_centre:
                    centre = r
                    r -= 1
                else:
                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1
        
        if centre > -1:
            swaps += abs(n//2-centre)
        
        return swaps
                    
                
