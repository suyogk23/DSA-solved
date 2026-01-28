# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        arr = []
        def inorder(node):
            nonlocal arr
            if not node:
                return
            inorder(node.left)
            # print(node.val)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        # print(arr)
        return arr[k-1]
