# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
solution by @suyogk23 GITHUB
traverese bfs 
append to a list when leaf node is encountered (list to be passed by reference as a parameter)
return if l1==l2 (corresponding to root1 and root2)
'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # bfs traversal
        def dfs(root, leaves):
            if not root.right and not root.left:
                leaves.append(root.val)
            if root.left:
                dfs(root.left, leaves)
            if root.right:
                dfs(root.right, leaves)
        
        l1, l2 = [], []
        if root1 and root2:
            dfs(root1, l1)
            dfs(root2, l2)
            return l1 == l2
        else:
            return False
