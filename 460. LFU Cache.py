class LFUCache:
    # will use hmap<freq, dll> and another hmap<key, self.DllNode> (frequency bucketing and maintaining lru in each freq bucket)
    class LRUcache:
        class DllNode:
            def __init__(self, key=-1, val=-1, prev=None, next=None, freq=0):
                self.key = key
                self.val = val 
                self.next = next
                self.prev = prev
                self.freq = freq

        def __init__(self, freq=0):
            self.head = self.DllNode() # lru
            self.tail = self.DllNode() # mru
            self.head.next = self.tail
            self.tail.prev = self.head
            self.hmap = {}
            self.freq = freq
        
        def get(self, key):
            if key in self.hmap:
                node = self.hmap[key]
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = self.tail
                node.prev = self.tail.prev
                self.tail.prev.next = node
                self.tail.prev = node

        def put(self, key, val):
            if key in self.hmap:
                self.get(key)
                self.hmap[key].val = val
            else:
                node = self.DllNode(key=key, val=val, freq=self.freq)
                node.next = self.tail
                node.prev = self.tail.prev
                self.tail.prev.next = node
                self.tail.prev = node
                self.hmap[key] = node
            return self.hmap[key]
        
        def delete(self, key):
            node = self.hmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
            del self.hmap[key]
        
        def evict(self):
            node = self.head.next
            key = node.key
            self.delete(key)
            return key
        
        def isEmpty(self):
            if self.head.next == self.tail:
                return True
            return False

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.cur_capacity = 0
        self.keyMap = {}
        self.freqMap = {} # freq:DLL
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        value, freq = self.keyMap[key].val, self.keyMap[key].freq
        # update in new freq bucket
        if freq + 1 not in self.freqMap:
            self.freqMap[freq + 1] = self.LRUcache(freq + 1)
        self.keyMap[key] = self.freqMap[freq+1].put(key, value)

        # delete from old freq bucket
        self.freqMap[freq].delete(key)
        if self.freqMap[freq].isEmpty():
            del self.freqMap[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.keyMap:
            if self.cur_capacity == self.max_capacity:
                # evict
                freq_bucket = self.freqMap[self.min_freq]
                evicted_key = freq_bucket.evict()
                del self.keyMap[evicted_key]
                if freq_bucket.isEmpty():
                    del freq_bucket
                    self.min_freq += 1 
                self.cur_capacity -= 1
            if 1 not in self.freqMap:
                # create a new freq bucket
                self.freqMap[1] = self.LRUcache(1) 
            # add the new key to freq bucket
            self.keyMap[key] = self.freqMap[1].put(key, value)
            self.min_freq = 1
            self.cur_capacity += 1
        else:
            self.get(key)
            self.keyMap[key].val = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 
