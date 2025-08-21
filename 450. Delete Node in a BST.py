# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
solution by @suyogk23 GITHUB
Recursively iterate in tree until key node is found,
When key node is found then replace current node value with max value in left sub tree (to retain BST property)
And delete the max node in left subtree
'''
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val: 
            root.left = self.deleteNode(root.left, key)
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key)
        else:
            #case when only 1 child node in left or right sub tree
            # the below cae also handles leaf node as l and r will be none hence returning none
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            #If there is left and right subree then find the max value in left sub tree
            if root.left:
                cur = root.left
                # find max value in left sub tree
                while cur.right:
                    cur = cur.right
                #replace current node val with max value in left sub tree
                root.val = cur.val
                root.left = self.deleteNode(root.left, cur.val)
            
        return root

            
