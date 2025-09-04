class Solution:
    # solution by @suyogk23 GITHUB
    # check for overlap (if i-1[1] < i[0])
    # if overlap check for right values i[1] and i-1[1]
    # remove the element with larger right value that way we can keep deletions to minimum
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        ans = 0
        i = 1
        while(i < len(intervals)):
            if (intervals[i][0] < intervals[i-1][1]):
                if intervals[i][1] > intervals[i-1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i-1)
                ans+=1
            else:
                i+=1
        
        return ans
