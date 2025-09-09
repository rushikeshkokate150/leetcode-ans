from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent = {}   # node -> parent
        visited = set()
        
        # Step 1: Build parent map
        def build_parent(root):
            q = deque([root])
            parent[root] = None
            while q:
                node = q.popleft()
                if node.left:
                    parent[node.left] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    q.append(node.right)
        
        # Step 2: BFS from target to find distance k
        def bfs(target, k):
            q = deque([target])
            visited.add(target)
            dist = 0
            while q:
                if dist == k:
                    return [n.val for n in q]  # collect values
                size = len(q)
                for _ in range(size):
                    node = q.popleft()
                    # Left
                    if node.left and node.left not in visited:
                        visited.add(node.left)
                        q.append(node.left)
                    # Right
                    if node.right and node.right not in visited:
                        visited.add(node.right)
                        q.append(node.right)
                    # Parent
                    if parent[node] and parent[node] not in visited:
                        visited.add(parent[node])
                        q.append(parent[node])
                dist += 1
            return []
        
        build_parent(root)
        return bfs(target, k)
