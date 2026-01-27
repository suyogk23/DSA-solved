# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l, r = min(p.val ,q.val), max(p.val, q.val)

        def getLCA(node):
            if not node:
                return None
            if node.val == l or node.val == r or (l < node.val and node.val<r):
                return node
            if node.val < l:
                return getLCA(node.right)
            if r < node.val:
                return getLCA(node.left)
        
        return getLCA(root)
