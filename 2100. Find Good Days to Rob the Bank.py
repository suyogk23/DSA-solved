class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # use downward slope length prefix array
        # use upward slope length postfix array
        # this is O(n + n + n) = O(n) linear solution
        n = len(security)
        if n == 0 or time > n//2 or time < 0:
            return []
        # calculate the length of downward slope at left of index
        down_slope_prefix_len = [0]*n
        for i in range(1, n):
            if security[i-1] >= security[i]:
                down_slope_prefix_len[i] = down_slope_prefix_len[i-1] + 1
        # calculate length of downward slope at right of index
        up_slope_prefix_len = [0]*n
        for j in range(n-1, 0, -1):
            if security[j-1] <= security[j]:
                up_slope_prefix_len[j-1] = up_slope_prefix_len[j] + 1
        # add valid days
        ans = []
        for k in range(time, n-time):
            if down_slope_prefix_len[k] >= time and up_slope_prefix_len[k] >= time:
                ans.append(k)

        return ans
