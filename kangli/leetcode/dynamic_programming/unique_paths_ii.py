class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        for i in range(1, m):
            if obstacleGrid[i - 1][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
        for j in range(1, n):
            if obstacleGrid[0][j - 1] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j - 1] and not obstacleGrid[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif obstacleGrid[i - 1][j] and not obstacleGrid[i][j - 1]:
                    dp[i][j] = dp[i][j - 1]
                elif obstacleGrid[i - 1][j] and obstacleGrid[i][j - 1]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

'''
Success
Details
Runtime: 40 ms, faster than 68.83% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.3 MB, less than 17.18% of Python3 online submissions for Unique Paths II.
Next challenges:
Unique Paths III

Related Topics: Array, Dynamic Programming
Similar Questions: Unique Paths, Unique Paths III
Hints:
1) The robot can only move either down or right. Hence any cell in the first row can only be reached 
from the cell left to it. However, if any cell has an obstacle, you don't let that cell contribute to any path. 
So, for the first row, the number of ways will simply be
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1] 
else
     obstacleGrid[i,j] = 0
You can do a similar processing for finding out the number of ways of reaching the cells in the first column.

2) For any other cell, we can find out the number of ways of reaching it, by making use of the number of ways
 of reaching the cell directly above it and the cell to the left of it in the grid. 
This is because these are the only two directions from which the robot can come to the current cell.

3) Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
else
     obstacleGrid[i,j] = 0
'''
