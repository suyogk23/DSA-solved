# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level, max_sum = 0, -float('inf')
        
        q = deque()
        cur_level = 1
        q.append([cur_level, root])

        while q:
            cur_sum = 0
            while q and q[0][0] == cur_level:
                front = q.popleft()
                node = front[1]
                cur_sum += node.val
                if node.left:
                    q.append([cur_level+1, node.left])
                if node.right:
                    q.append([cur_level+1, node.right])
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_level = cur_level
            cur_level+=1
            
        
        return max_level
            
