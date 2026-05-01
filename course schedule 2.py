class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited  = [0]*numCourses
        pathvisted = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        ans = []

        for i in prerequisites:
            adj[i[1]].append(i[0])
            # print(i)


        def dfs(node):
            visited[node] = 1
            pathvisted[node] = 1
            for  i in adj[node]:
                if not visited[i]:
                    if dfs(i) == False:
                        return False
                elif visited[i] and pathvisted[i] == 0:
                    continue
                elif visited[i] and pathvisted[i] == 1 :
                    return False
            pathvisted[node] = 0
            ans.append(node)
            return True

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i) == False:
                    return []
        return ans[::-1]