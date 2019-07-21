########## O(mlogn) #############
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # No duplicate integers in each row or column.
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0 
        m, n = len(matrix), len(matrix[0])
        self.result = 0
        for row in range(m):
            if matrix[row][0] == target:
                self.result += 1 
                break
            if matrix[row][-1] == target:
                self.result += 1 
                continue
            if matrix[row][0] < target < matrix[row][-1]:
                self.search_on_row(matrix[row], target, 0, n - 1)
                
        return self.result 
        
    def search_on_row(self, array, target, left, right):
        start, end = left, right
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if array[mid] == target:
                self.result += 1 
                return 
            elif array[mid] < target:
                start = mid 
            else:
                end = mid 
                
        if array[start] == target or array[end] == target:
            self.result += 1 
            
        return
        
######## O(m+n) #################
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # O(m + n), from left bottom to right top
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0 
            
        result = 0 
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] == target:
                result += 1 
                row -= 1 
                col += 1 
            elif matrix[row][col] > target:
                row -= 1 
            else:
                col += 1 
                
        return result 
