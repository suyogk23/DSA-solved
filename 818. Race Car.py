class Solution:
    def racecar(self, target: int) -> int:
        # imagine a graph with increasing slope as we accelerate
        # we keep accelerating until we reach target or exceed target
        # if we exceed target, we have to check from prev num we were at before exceeding the target, 
        # we Reverse at this position and reset our exponential acceleration rate (this may look like RR or RAR, depending on the condition)
        # we again accelerate until we reach our target
        # now how do we determine the minimum num of operations(steps) to reach target
        # we use djikstras
        # effectively we store (steps, pos, speed) the min heap, we auto choose the least step options first, and if we over shoot with same num of steps 
        # we choose the path in which we do not overshoot with same num of stpes as pos(not overshoot) < pos(overshoot)
        # in a way we are searching for nodes (pos, speed) with least num of steps
        # TC: O(target * log^2(target)), as there are log(target) possible speed for n < target positions, and each heap operaion takes log(n)
        # Space: O(target * log(target)), as we consider nodes as (pos, speed), again for each pos, log(target) speeds are possible and upto target  number of positions are possible
        # this means number of states = all possible positions * all possible speed from that position

        pq = [(0, 0, 1)] #(steps, pos, speed) # first step is to always accelerate
        heapq.heapify(pq)
        vis = set()

        while pq:
            steps, pos, speed = heapq.heappop(pq)
            vis.add((pos, speed))
            if pos == target:
                return steps

            next_pos = pos + speed
            next_speed = speed * 2

            heapq.heappush(pq, (steps+1, next_pos, next_speed)) # accelerate

            # if overshoot or going in negative direction(away from target), then reverse (change direction)
            if (next_pos > target and next_speed > 0) or (next_pos < target and next_speed < 0):
                next_speed = -1 if speed > 0 else 1
                heapq.heappush(pq, (steps+1, pos, next_speed))



        
