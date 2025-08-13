class Solution:
    '''
    # 3D dp, use lru_cache(None)
    # base case l > r: return 0
    # case 1: check subsequent equal elements and calculate points
    # case 2: check non subsequent equal elements and the subarray in between and calculate points
    # ans = max(case 1, case 2)
    '''
    # solution by suyogk@23 GITHUB
    def removeBoxes(self, boxes: List[int]) -> int:
        l, r = 0, len(boxes)-1
        @lru_cache(None)
        def dp(l, r, count):
            if l > r:
                return 0
            while l < r and boxes[l]==boxes[l+1]:
                count+=1
                l+=1
            ans = (count+1)**2 + dp(l+1, r, 0)
            for i in range(l+1, r+1):
                if boxes[l] == boxes[i]:
                    ans = max(ans, dp(i, r, count+1)+dp(l+1, i-1, 0))
            return ans
        
        ans = dp(l, r, 0)
        return ans

