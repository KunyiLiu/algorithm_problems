class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # dp[i][j]- the min sum from the first point to (i,j)
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0 
            
        m, n = len(grid), len(grid[0])
        
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

                
                
        return dp[m-1][n-1]
