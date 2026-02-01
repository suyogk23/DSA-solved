class LRUCache:
    class DllNode:
        def __init__(self, key=-1, val=-1, prev=None, next=None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.cur_capacity = 0
        self.max_capacity = capacity
        self.head = self.DllNode()
        self.tail = self.DllNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hmap = {}

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        # swap
        self.hmap[key].prev.next = self.hmap[key].next
        self.hmap[key].next.prev = self.hmap[key].prev
        self.hmap[key].next = self.tail
        self.hmap[key].prev = self.tail.prev
        self.tail.prev.next = self.hmap[key]
        self.tail.prev = self.hmap[key]
        return self.hmap[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.hmap: 
            if self.cur_capacity == self.max_capacity:
                #evict LRU
                lru = self.head.next
                self.head.next = lru.next
                lru.next.prev = self.head
                del self.hmap[lru.key]
                lru.next = lru.prev = None
                self.cur_capacity -= 1
            # insert the new key
            new_node = self.DllNode(key=key, val=value, prev=self.tail.prev, next=self.tail)
            self.tail.prev.next = new_node
            self.tail.prev = new_node
            self.hmap[key] = new_node
            self.cur_capacity += 1

        else:
            self.get(key)
            self.hmap[key].val = value
            return

        

