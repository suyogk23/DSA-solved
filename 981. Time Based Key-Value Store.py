class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: #O(1)
        self.hm[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str: #O(n)
        # linear search the most recent timestamp 
        for ele in self.hm[key][::-1]:
            ts = ele[0]
            val = ele[1]
            if ts <= timestamp:
                return val
        return 
        


