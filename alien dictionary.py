k = 4
arr = ["baa","abcd","abca","cab","cad"]

adj = [[] for _ in range(k)]

# Build graph
for i in range(len(arr)-1):
    s1 = arr[i]
    s2 = arr[i+1]

    j = 0

    while j < min(len(s1), len(s2)) and s1[j] == s2[j]:
        j += 1

    if j < min(len(s1), len(s2)):
        adj[ord(s1[j]) - ord('a')].append(
            ord(s2[j]) - ord('a')
        )

# DFS Topological Sort
def dfs(node, stack):
    visited[node] = 1

    for nei in adj[node]:
        if not visited[nei]:
            dfs(nei, stack)

    stack.append(chr(node + ord('a')))

stack = []
visited = [0] * k

for i in range(k):
    if not visited[i]:
        dfs(i, stack)

print(stack[::-1])