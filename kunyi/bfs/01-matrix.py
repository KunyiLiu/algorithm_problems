#################### BFS #################
class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def updateMatrix(self, matrix):
        # reverse source and destination
        # record the neareast distance from 0 to other cells 
        # T(n) = mn
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
            
        m, n = len(matrix), len(matrix[0])
        result = [[-1]*n for i in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                    result[i][j] = 0
                    
        distance = 1 
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                x, y = queue.pop(0)
                for j in range(4):
                    new_x = delta_X[j] + x 
                    new_y = delta_Y[j] + y  
                    if 0<= new_x < m and 0 <= new_y < n and result[new_x][new_y] == -1:
                        queue.append((new_x, new_y))
                        result[new_x][new_y] = distance
                        
            distance += 1 
            
############ DP 从左上出发推一遍。 从右下出发推一遍。#################### 
class Solution:
    """
    @param matrix: a 0-1 matrix
    @return: return a matrix
    """
    def updateMatrix(self, matrix):
        # write your code here
        n, m = len(matrix), len(matrix[0])
        dp = [[100000 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if (matrix[i][j] == 0):
                    dp[i][j] = 0
                if (i > 0):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if (j > 0):
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if (dp[i][j] > 0):
                    if (i < n - 1):
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                    if (j < m - 1):
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
