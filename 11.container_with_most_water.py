class Solution:
    # calculate the area of rectangle based on smaller height
    # whicherver height is smaller move it to right or left
    def maxArea(self, height: List[int]) -> int:
        right = len(height)-1
        left = 0
        max_area = 0

        while(left < right):
            cur_area = 0
            if (height[left] > height[right]):
                cur_area = height[right]*(right-left)
                right-=1
            elif (height[left] < height[right]):
                cur_area = height[left]*(right-left)
                left+=1
            else:
                #move either as both sides are equal
                cur_area = height[right]*(right-left)
                left+=1
            max_area = max(cur_area, max_area)
        
        return max_area




        

