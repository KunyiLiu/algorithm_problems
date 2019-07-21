class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # O(mn)
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]* n for i in range(m)]
        self.dp[0][0] = matrix[0][0]
        for i in range(1, n):
            self.dp[0][i] = self.dp[0][i-1] + matrix[0][i]
            
        for i in range(1, m):
            self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i][j] - self.dp[i-1][j-1]
        
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        upper = self.dp[row1-1][col2] if row1 >= 1 else 0
        left = self.dp[row2][col1-1] if col1 >= 1 else 0 
        overlap = self.dp[row1-1][col1-1] if row1 >= 1 and col1 >= 1 else 0
        return self.dp[row2][col2] - upper - left + overlap
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
