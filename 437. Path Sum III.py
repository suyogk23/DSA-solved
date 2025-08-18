# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2 paths: 1 always includes current node val, other always excludes curr nodes values
# dfs(): include current node val, continue to do so until entire subtree is traversed
# self.pathSum() in return stmt always excludes current val in all subseq calls in the subtree
# solution by @suyogk23 GITHUB
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(root, pathSum):
            if not root:
                return 0
            pathSum += root.val
            if pathSum == targetSum:
                return 1 + dfs(root.left, pathSum) + dfs(root.right, pathSum)
            else:
                return dfs(root.left, pathSum) + dfs(root.right, pathSum)
        
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
