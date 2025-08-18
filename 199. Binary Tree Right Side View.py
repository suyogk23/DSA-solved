# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Solution by @suyogk23 GITHUB
- Use BFS
- Check for right most node by checking the last node appended at that level
- use a for loop with current size of queue (as at beginning of each while loop q will all have elements of that level)
- when i == size-1 in for loop, it indicates the last element of that level
- append value of this node to answer list. 
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                #last node of this level (right most node because of bfs)
                if i == size-1:
                    ans.append(node.val)
        return ans
