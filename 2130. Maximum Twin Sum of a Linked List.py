# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(1) solution
# find len of linked list
# traverse 1 more than first half of linked list
# reverse the linked list from this node
# now you have head and tail of linked list
# traverse n/2 times and update max twin sum each iteration accordingly

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get size of linked list
        node = head
        n = 0
        while(node):
            node = node.next
            n += 1
        # traverse until half + 1 element of linked list
        node = head
        i = 0
        while(i < ((n/2))):
            node = node.next
            i += 1
        # reverse the second half of linked list
        prev = node
        node = node.next
        while(node):
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        trail = prev
        # traverse for n/2 times and update the max_twin_sum accordingly
        l, r = head, prev
        i = 0
        maxTsum = 0
        while(i < n/2):
            maxTsum = max(maxTsum, l.val + r.val)
            l = l.next
            r = r.next
            i += 1
        return maxTsum



