class RecentCounter:
    '''
    Use a queue to track the pings that fall in range [t-3000, t]
    if they dont fall in range remove them in LIFO order
    return len of queue, because the queue will have all the elements that fall in range [t-3000, t]
    solution by @suyogk23 GITHUB
    '''
    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t-3000:
            self.q.pop(0)
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
