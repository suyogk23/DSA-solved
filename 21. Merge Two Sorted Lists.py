# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        new_head = ListNode()
        cur = new_head
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = ListNode(val=p1.val)
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = ListNode(val=p2.val)
                cur = cur.next
                p2 = p2.next
        while p1:
            cur.next = ListNode(val=p1.val)
            cur = cur.next
            p1 = p1.next
        while p2:
            cur.next = ListNode(val=p2.val)
            cur = cur.next
            p2 = p2.next
            
        return new_head.next
