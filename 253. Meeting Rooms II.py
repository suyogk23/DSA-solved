"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# solution by @suyogk23 GITHUB
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # store start and end times in seperate arrays
        start_times = [i.start for i in intervals]
        end_times = [i.end for i in intervals]
        # sort these arrays
        start_times = sorted(start_times)
        end_times = sorted(end_times)
        # use 2 pointer 1 for each array and maintain a count and max_count variable
        # loop until start_times is fully traversed
        # move s if start time is lesser than current end time, meeting has not ended so increase number of days/rooms as overlapping time do count+1  
        # else move e, do count - 1 as 1 meeting has concluded and 1 day/room is free for other meets
        s, e = 0, 0
        count, max_count = 0, 0
        n = len(intervals)

        while s < n:
            if start_times[s] < end_times[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            max_count = max(count, max_count)

        return max_count
