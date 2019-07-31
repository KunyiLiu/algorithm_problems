class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        # longest seq with 1 
        left, up = [[0] * n for i in range(m)], [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0 and matrix[i][j] == '1':
                    left[i][j] = 1
                elif j > 0:
                    left[i][j] = 0 if matrix[i][j] == '0' else left[i][j-1] + 1 
                    
        for i in range(n):
            for j in range(m):
                if j == 0 and matrix[j][i] == '1':
                    up[j][i] = 1 
                elif j > 0:
                    up[j][i] = 0 if matrix[j][i] == '0' else up[j-1][i] + 1 
        
        def is_valid(i, j, k):
            if i-k+1 < 0 or j-k+1 < 0:
                return False
            for x in range(i-k+1, i):
                if left[x][j] < k:
                    return False
            for y in range(j-k+1, j):
                if up[i][y] < k:
                    return False
                
            return True
            
        
        result = 0 
        for i in range(m):
            for j in range(n):
                if result >= min(left[i][j], up[i][j]):
                    continue
                for k in range(min(left[i][j], up[i][j]), result, -1):
                    if is_valid(i, j, k):
                        result = k
                        
        return result*result
