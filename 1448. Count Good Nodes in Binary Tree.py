# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# solution @suyogk23 GITHUB
# keep updating max_val and return left + right subtree +1 if current node is greater than max_val, 
# else only return left + right without adding 1
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_val):
            left, right = 0, 0
            if root.left:
                left = dfs(root.left, max(max_val, root.val))
            if root.right:
                right = dfs(root.right, max(max_val, root.val))
            if root.val >= max_val:
                return 1 + left + right
            else:
                return left + right
        return dfs(root, -10**4-1) #-10^4+1 is lower bound
            
                

        
