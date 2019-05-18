import sys
class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # lower bound, upper bound 
        # sum[i][j] = sum[0][j] + sum[1][j] + ... + sum[i][j]
        sum_res = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        for top in range(m):
            _sum = [0] * n 
            for down in range(top, m):
                prefix_sum = [0] * (n+1)
                for col in range(n):
                    _sum[col] += matrix[down][col]
                    prefix_sum[col+1] = prefix_sum[col] + _sum[col]
                # old find max subarray 
                tmp_sum = self.find_max(prefix_sum)
                sum_res = max(tmp_sum, sum_res)
                
        return sum_res
        
    def find_max(self, sum_list):
        prefix_sum = sum_list[0] 
        tmp_sum = - sys.maxsize
        for i in range(len(sum_list)):
            tmp_sum = max(tmp_sum, sum_list[i] - prefix_sum)
            prefix_sum = min(prefix_sum, sum_list[i])
            
        return tmp_sum
        
        
 ####### another way of doing max subarray ###########
import sys
class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # lower bound, upper bound 
        # sum[i][j] = sum[0][j] + sum[1][j] + ... + sum[i][j]
        sum_res = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        for top in range(m):
            arr = [0] * n 
            for down in range(top, m):
                for col in range(n):
                    arr[col] += matrix[down][col]
                # old find max subarray 
                tmp_sum = self.find_max(arr)
                sum_res = max(tmp_sum, sum_res)
                
        return sum_res
        
    def find_max(self, arrays):
        total_sum = 0 
        res = 0 
        for i in range(len(arrays)):
            total_sum += arrays[i]
            res = max(res, total_sum)
            total_sum = max(total_sum, 0)
            
        return res
