# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solution by @suyogk23 GITHUB
    # in place O(n)
    # careful reassignment and temp storage of pointers
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy_node = ListNode(next=head)
        prev, cur = dummy_node, dummy_node.next
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head = prev
        dummy_node.next.next = None
        return head

