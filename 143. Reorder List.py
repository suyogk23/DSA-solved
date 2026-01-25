# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split list in half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        # reverse the second half
        prev, nxt = None, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # merge the 2 linked lists alternatively
        h1, h2 = head, prev
        while h1 and h2:
            n1 = h1.next
            n2 = h2.next
            h1.next = h2
            h2.next = n1
            h1 = n1
            h2 = n2
