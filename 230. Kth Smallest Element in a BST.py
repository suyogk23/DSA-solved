# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        ans = None
        def inorder(node):
            nonlocal ans
            nonlocal k
            if not node or ans != None:
                return
            inorder(node.left)
            k-=1
            if k == 0:
                ans = node.val
                return 
            if k < 0:
                return
            inorder(node.right)
        inorder(root)

        return ans
