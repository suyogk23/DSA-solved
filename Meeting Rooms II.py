"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort array
        # crux: in case of overlap, days += 1 and keep track of min end times using min heap
        # in case cur start >= heap[0] then pop the min val from heap
        n = len(intervals)
        if n == 0:
            return 0
        days = 1
        intervals.sort(key=lambda x:x.start) # O(n log n)
        prev = intervals[0]
        hq = [prev.end]

        for i in range(1, n):
            cur = intervals[i]
            if hq[0] > cur.start:    # overlap
                days += 1  
            else:
                heapq.heappop(hq)
            heapq.heappush(hq, cur.end)
        
        return days




        
