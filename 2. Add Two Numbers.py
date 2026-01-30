# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s//10
            s = s%10
            cur.next = ListNode(val=s)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + carry
            carry = s // 10
            s = s%10
            cur.next = ListNode(val = s)
            l1 = l1.next
            cur = cur.next

        while l2:
            s = l2.val + carry
            carry = s // 10
            s = s%10
            cur.next = ListNode(val = s)
            l2 = l2.next
            cur = cur.next
        
        if carry > 0:
            cur.next = ListNode(val=carry)
        
        return dummy.next
        
