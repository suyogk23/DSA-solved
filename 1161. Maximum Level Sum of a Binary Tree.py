# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # solution by @suyogk23 GITHUB
    # do bfs traversal, for each level calculate sum
    # if cur level sum is the max then update the max_level var
    # hint: traverse node in cur level: for i in range(len(q))
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level, max_sum = 0, -float('inf')
        
        q = deque()
        cur_level = 1
        q.append(root)

        while q:
            cur_sum = 0
            level_node_count = len(q)
            for i in range(level_node_count): # iterates only for nodes at cur level
                node = q.popleft()
                cur_sum += node.val
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            if cur_sum > max_sum:
                max_level = cur_level
                max_sum = cur_sum
            cur_level+=1
            
        
        return max_level
            
