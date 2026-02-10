class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        #TC: O(n + q)
        # Space: O(n + q)
        n = len(s)

        # nearest left candle
        nearest_left_candle = [-1]*n
        prev = -1
        for i in range(n):
            if s[i] == '|':
                prev = i
            nearest_left_candle[i] = prev
        # nearest right candle
        nearest_right_candle = [-1]*n
        nxt = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                nxt = i
            nearest_right_candle[i] = nxt
        # calculate prefix sum of plates
        plate_prefix_sum = [0]*n
        if s[0] == '*':
            plate_prefix_sum[0] = 1
        for i in range(1, n):
            if s[i] == '*':
                plate_prefix_sum[i] = plate_prefix_sum[i-1] + 1
            else:
                plate_prefix_sum[i] = plate_prefix_sum[i-1]
        
        # for each l, r in query fing nearest right for l and nearest left for r
        # calcualate num of plates using the plates prefix sum for max candle range fitting
        # ql <= left and qr >= right -(visulaization)-> [ql[left, right]qr]
        ans = []
        for ql, qr in queries:
            left = nearest_right_candle[ql]
            right = nearest_left_candle[qr]
            if left == -1 or right == -1 or left >= right:
                num_plates = 0
            else:
                num_plates = plate_prefix_sum[right] - plate_prefix_sum[left]
            ans.append(num_plates)

        return ans 
