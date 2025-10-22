# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # solution by @suyogk23 GITHUB
        # do dfs traversal, if node == p or q it is LCA (as the other node has to be below it accordign to Leetcode contraints)
        # if node is none return none
        # if left node == p or q, return left node, if right node == p or q return right node
        # if left or right subtree does not contian p or q, return None
        # if left subtree is none, p or q must be in right subtree as per constraints
        # if right subtree is none, p or q must be in left subtree as per constraints
        
        def dfs(node, p, q):
            if not node or node == p or node == q:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if not right:
                return left
            elif not left:
                return right
            else:
                return node
        
        return dfs(root, p, q)
