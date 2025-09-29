# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time and space
# append to list and find max sum (maintain l and r pointer at both ends)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        l = []
        while(node):
            l.append(node.val)
            node = node.next
        n = len(l)
        i, j = 0, n-1
        ans = 0
        while(i < j):
            ans = max(ans, (l[i] + l[j]))
            i += 1
            j -= 1
        
        return ans
