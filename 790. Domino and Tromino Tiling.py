class Solution:
    # solution by @suyogk@23
    def numTilings(self, n: int) -> int:
        '''
        this is pattern based dp
        consider subproblem reccurance relation:
        full[i] = full[i-1] + full[i-1] + top_mising[i-1] + bottom_missing[i-1]
        top_missing[i] = full[i-2] + bottom_missing[i-1]
        bottom_missing[i] = full[i-2] + top_missing[i-1]

        need to return full[n] as this is the total combination to form a full n sized domino and tromino tiles
        '''
        prev_prev_full, prev_full, full = 1, 1, n
        prev_bottom_missing, bottom_missing = 0, 0
        prev_top_missing, top_missing = 0, 0
        for i in range(2, n+1):
            full = prev_prev_full + prev_full + prev_top_missing + prev_bottom_missing
            top_missing = prev_prev_full + prev_bottom_missing
            bottom_missing = prev_prev_full + prev_top_missing

            prev_prev_full = prev_full
            prev_full = full
            prev_top_missing = top_missing
            prev_bottom_missing = bottom_missing
        
        return full % (10**9 + 7)


        
        
