"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = [root]
        q = deque(q)

        while q:
            level = len(q)
            prev = q.popleft()
            if prev.left:
                q.append(prev.left)
            if prev.right:
                q.append(prev.right)
            for _ in range(level-1):
                nxt = q.popleft()
                prev.next = nxt
                prev = prev.next
                if nxt.left:
                    q.append(nxt.left)
                if nxt.right:
                    q.append(nxt.right)
        return root
        
