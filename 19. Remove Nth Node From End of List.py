# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use fast and slow ptr such that the fast ptr is n nodes ahead of slow ptr
        # traverse until fast node reaches last node
        # this way slow ptr alwasy ends at n-1 th position
        # proceed with removal of nth node
        
        dummy = ListNode(val=0, next=head) # handles some edge cases
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        # move fast ptr until last node, slow ptr will be at n-1 pos ( EXCEPT EDGE CASE n=len(list))
        while fast.next:
            slow=slow.next
            fast = fast.next
        # remove n th node
        slow.next = slow.next.next
        return dummy.next
        
        
