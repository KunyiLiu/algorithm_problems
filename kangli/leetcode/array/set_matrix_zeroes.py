class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] = 0
                if j in col:
                    matrix[i][j] = 0 
        

'''
Success
Details 
Runtime: 136 ms, faster than 100.00% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.6 MB, less than 5.11% of Python3 online submissions for Set Matrix Zeroes.
Next challenges: Game of Life
'''
