from collections import deque
def bfs(graph, start):
    visited = set()            
    queue = deque([start])     
    visited.add(start)
    while queue:
        node = queue.popleft()  
        print(node)             

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)                               #[]
                queue.append(neighbor)                              #out put=ABCDEF
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


bfs(graph, 'A')

# from collections import deque
# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def _init_(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[List[int]]
#         """
#         ans = []
#         if not root:
#             return ans

#         q = deque([root])
        
#         while q:
#             level = []
#             size = len(q)
#             for i in range(size):
#                 node = q.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             ans.append(level)
        
#         return ans