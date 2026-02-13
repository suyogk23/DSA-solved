class Solution:
    def appealSum(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)

        # subproblem: @ s[i], the total appeal is:
        # if s[i] is never seen before: appeal(s[i-1]) + (i+1) [total appeal increases by +1 for all prev substrs]
        # else: appeal(s[i-1]) + (i - rev_idx_s[i]) [total appeal increases by +1 only for substrs where s[i] has not occured before]
        # the above 2 cases also handles the individual appeals for substr with length 1
        # accumulate prev accross all idx, as the prev will contain appeal for all substr only unitl idx i
        # why?: by combinatorics: the increment in appeal is defined as above (theory)

        prev_seen_idx = {}
        prev_appeal = 0
        total_appeal = 0
        for i, c in enumerate(s):
            if c in prev_seen_idx:
                # seen previously
                prev_appeal = prev_appeal + (i - prev_seen_idx[c])
            else:
                prev_appeal = prev_appeal + (i + 1)
            prev_seen_idx[c] = i
            total_appeal += prev_appeal

        return total_appeal

        
