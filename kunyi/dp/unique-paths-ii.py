class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[m-1][n-1]
