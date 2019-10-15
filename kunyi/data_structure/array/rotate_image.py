class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # rule - (i, j) -> (j, n - 1 - i)
        # from outside to inside 
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range(n):
            matrix[i].reverse()
