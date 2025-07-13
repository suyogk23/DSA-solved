class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = {}
        
        for i in range(len(arr)):
            if arr[i] not in hash_map:
                hash_map[arr[i]] = 1
            hash_map[arr[i]]+=1

        #get all values from dict as list
        values = list(hash_map.values())
        hash_set = set()
        for i in values:
            if i in hash_set:
                return False
            hash_set.add(i)
        return True
    

    