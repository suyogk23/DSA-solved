# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution by @suyogk23 GITHUB
    '''
    If get min of root of left and root of right and also for each branch add 1 while returning
    '''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root.left and not root.right:
                return 1
            if not root.left:
                return 1+dfs(root.right)
            if not root.right:
                return 1+dfs(root.left)
            return 1+min(dfs(root.left), dfs(root.right))
        
        return dfs(root)
        
