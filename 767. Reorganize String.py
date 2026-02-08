from math import ceil
class Solution:
    def reorganizeString(self, s: str) -> str:
        # maintain max heap with (count, char), keep adding the top 2 most freq chars to ans
        # push the char with updated count to heap again
        # TC: O(n)
        # Space: O(n)
        n = len(s)
        hm = defaultdict(int)
        
        for c in s:
            hm[c] += 1
        # check if rearrangement is possible:
        max_count = max(list(hm.values()))
        # print(count, (n-count))
        if max_count > ceil(n/2): # count(cur_ele) - count(remaining_ele)
            print(max_count)
            return ""

        pq = []
        for char, count in hm.items():
            heapq.heappush(pq, [-count, char]) # max heap is min heap with negative values
        
        ans = ""

        while len(pq) >= 2:
            count1, char1 = heapq.heappop(pq)
            count2, char2 = heapq.heappop(pq)
            ans = ans + char1 + char2
            count1 += 1
            count2 += 1
            if count1 < 0:
                heapq.heappush(pq, [count1, char1])
            if count2 < 0:
                heapq.heappush(pq, [count2, char2])
        if pq:
            ans = ans + heapq.heappop(pq)[1]

        return ans
