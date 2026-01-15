class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hmap = {}
        for p, s in zip(position, speed):
            hmap[p] = s
        tn, tc = 0, 0
        fleet = 0
        for k in sorted(hmap.keys(), reverse=True):
            tc = (target-k)/hmap[k]
            if tc > tn:
                tn = tc
                fleet += 1
        return fleet
            
