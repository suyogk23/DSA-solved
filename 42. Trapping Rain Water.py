class Solution:
    # this is a Two Pointer problem
    # track max left height and right height so far, 
    # move ptr that has lesser height
    # update max left or right height (do this before calculating area)
    # calcualte cur vol, max height - cur height, add cur vol to toal vol
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        
        l = 0
        r = n-1
        max_left_height = height[l]
        max_right_height = height[r]
        total_vol = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left_height = max(max_left_height, height[l])
                cur_vol = max_left_height - height[l]
                total_vol += cur_vol
            else:
                r -= 1
                max_right_height = max(max_right_height, height[r])
                cur_vol = max_right_height - height[r]
                total_vol += cur_vol
        
        return total_vol
