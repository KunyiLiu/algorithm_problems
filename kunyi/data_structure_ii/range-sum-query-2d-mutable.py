class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m, self.n = len(matrix), len(matrix[0])
        self.bits = [[0] * (self.n+1) for i in range(self.m+1)]
        self.matrix = matrix
        for i in range(self.m):
            for j in range(self.n):
                self.add(i, j, self.matrix[i][j])
            
                
    def lowbit(self, x):
        return x & (-x)
                
    def add(self, i, j, val):
        # note: level 
        ind_x = i + 1
        while ind_x <= self.m:
            ind_y = j + 1 
            while ind_y <= self.n:
                self.bits[ind_x][ind_y] += val 
                ind_y += self.lowbit(ind_y)
            ind_x += self.lowbit(ind_x)
    
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val 
        self.add(row, col, diff)
        
    def get_prefix_sum(self, row, col):
        tmp_sum = 0
        ind_x = row + 1
        while ind_x > 0:
            ind_y = col + 1 
            while ind_y > 0:
                tmp_sum += self.bits[ind_x][ind_y]
                ind_y -= self.lowbit(ind_y)
            ind_x -= self.lowbit(ind_x)
        return tmp_sum


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.get_prefix_sum(row2, col2) - self.get_prefix_sum(row1 - 1, col2) - self.get_prefix_sum(row2, col1 - 1) + self.get_prefix_sum(row1-1, col1-1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
