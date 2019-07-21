class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False 
            
        m, n = len(matrix), len(matrix[0])
        # find the last row where first element <= target
        start, end = 0, m - 1 
        target_row = -1
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if matrix[mid][0] <= target:
                start = mid 
            else:
                end = mid 
                
        if matrix[end][0] <= target:
            target_row = end
        elif matrix[start][0] <= target:
            target_row = start 
        else:
            return False 
            
        # find the value on the target_row
        start, end = 0, n - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if matrix[target_row][mid] == target:
                return True 
            elif matrix[target_row][mid] > target:
                end = mid 
            else:
                start = mid 
                
        if target in [matrix[target_row][start], matrix[target_row][end]]:
            return True 
        
        return False
