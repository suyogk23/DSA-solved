# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        pq = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, [head.val, i, head])

        cur = dummy = ListNode()
        while pq:
            ele = heapq.heappop(pq)
            cur.next = ele[2]
            ele[2] = ele[2].next
            cur = cur.next
            if ele[2]:
                ele[0] = ele[2].val
                heapq.heappush(pq, ele)

        return dummy.next
