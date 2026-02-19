class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def path(i,j,dp):

            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0
            elif i == 0 and j == 0:
                return 1
            elif i < 0 or j < 0:
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            
            up = path(i-1,j,dp)
            left = path(i,j-1,dp)
            
            dp[i][j] = up+left
            
            return dp[i][j]
            
        return path(m-1,n-1,dp)