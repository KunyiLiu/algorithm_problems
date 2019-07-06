class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

'''
Success
Details
Runtime: 48 ms, faster than 15.12% of Python3 online submissions for Unique Paths.
Memory Usage: 13.1 MB, less than 69.55% of Python3 online submissions for Unique Paths.
Next challenges:
Unique Paths II
Minimum Path Sum
Dungeon Game

Related Topics: Array, Dynamic Programming
Similar Questions: Unique Paths II, Minimum Path Sum, Dungeon Game
'''
