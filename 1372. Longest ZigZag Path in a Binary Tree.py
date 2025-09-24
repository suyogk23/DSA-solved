# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution by @suyogk23 GITHUB
    # maintain a path var for ever node you start
    # in each node, 
    # if node is a left child go to right child of cur node and add +1 to path
    # and start again as a start node and zigzag traverse left child
    # if node is a rght child go to left child of cur node and add +1 to path
    # and start again as a start node and zigzag traverse right child
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxpath = 0
        def getMax(node, flag, path):
            nonlocal maxpath
            if not node:
                return
            maxpath = max(maxpath, path)
            if flag == 'l': # cur node is left child
                #go right
                getMax(node.right, 'r', path+1)
                # start path measurement again
                getMax(node.left, 'l', 1)    
            else: # cur node is a right child
                #go left
                getMax(node.left, 'l', path+1)
                # start path measurement again
                getMax(node.right, 'r', 1)
        getMax(root, 'l', 0)
        return maxpath
