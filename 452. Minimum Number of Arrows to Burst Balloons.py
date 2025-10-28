class Solution:
    # solution by @suyogk23 GITHUB
    # sort the array with Xstart as the key
    # if the current element end is greater than or equal to next element start, merge it
    # keep track of minimum end (or right) as this is crucial for arraows to burst baloons
    # for each merged intervals count one arrow
    # iterate linearly
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:x[1])
        num_arrows = 0
        n = len(points)
        i=0
        while i<n:
            r = points[i][1]
            while i<n-1 and points[i+1][0] <= r:
                r = min(r, points[i+1][1])
                i+=1   
            num_arrows+=1
            i+=1
        # print(num_arrows)
        return num_arrows
