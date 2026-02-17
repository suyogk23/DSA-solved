from math import ceil
class TimeMap:
    
    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: #O(1)
        self.hm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str: #O(log n)
        # binary search the most recent timestamp 
        # monotonic search space on left
        values = self.hm[key]
        n = len(values)
        l, r = 0, n-1
        while l < r:
            m = ceil((l+r)/2)
            # print(l, r, m)
            if values[m][0] <= timestamp:
                l = m 
            else:
                r = m - 1
        if not values or values[l][0] > timestamp:
            print(l)
            return 
        return values[l][1]     


