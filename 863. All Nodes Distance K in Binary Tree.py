# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # convert tree to graph and do bfs until k level
    # return the nodes at k level in list
    # TC : O(n) tree dfs traversal + O(n) graph bfs traversal, TC: O(n)
    # Space: O(n) because tree has maximum 2(n-1) edges where n is num of nodes, so space complexity is O(E + V), which is O(n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # construct graph
        adj = defaultdict(list)
        def dfs(node):
            nonlocal adj
            if not node:
                return
            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans = []
        q = deque([target.val])
        vis = set([target.val])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if k == 0:
                    ans.append(node)
                for n in adj[node]:
                    if n not in vis:
                        q.append(n)
                        vis.add(n)
            if k == 0:
                return ans
            k-=1
        
        return ans

