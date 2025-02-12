class Solution:
    # 2 ptr optimal:
    # so we have l = start, r = end
    # we move whicever one is smaller becuase imagine left =3 and right = 4 
    # so whatever is in between can have max 3 u of water - height in current cell, 
    # so basically this is why we shift whichever height is lower(i.e, l or r)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if (n<=2):
            return 0

        maxL = height[0]
        maxR = height[n-1]
        l, r = 0, n-1
        vol = 0
        while (l < r):
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                vol += maxL - height[l]
            else:
                r -= 1 
                maxR = max(maxR, height[r])
                vol += maxR - height[r]

        return vol



