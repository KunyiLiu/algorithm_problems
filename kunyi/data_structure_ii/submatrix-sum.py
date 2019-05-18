class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
    # 用前缀和优化, 令 sum[i][j] = sum[0][j] + sum[1][j] + ... + sum[i][j]
    # 然后枚举上下边界, 这样就相当于在一行内, 求一个数组连续子串和为0的问题了.
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
            
        m, n = len(matrix), len(matrix[0])
        for top in range(m):
            _sum = [0] * n 
            for down in range(top, m):
                prefix_hash = {0: -1}
                prefix_sum = 0 
                for col in range(n):
                    _sum[col] += matrix[down][col]
                    prefix_sum += _sum[col]
                    if prefix_sum in prefix_hash:
                        return [[top, prefix_hash[prefix_sum] + 1], [down, col]]
                    prefix_hash[prefix_sum] = col 
                    
        return None
