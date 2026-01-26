# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None

        def mergeSortedLL(n1, n2):
            cur = dummy = ListNode()
            while n1 and n2:
                if n1.val <= n2.val:
                    cur.next = n1
                    cur = cur.next
                    n1 = n1.next
                else:
                    cur.next = n2
                    cur = cur.next
                    n2 = n2.next
            if n1:
                cur.next = n1
            else:
                cur.next = n2
            return dummy.next

        cur = lists[0]
        for i in range(1, n):
            cur = mergeSortedLL(cur, lists[i])

        return cur

         
