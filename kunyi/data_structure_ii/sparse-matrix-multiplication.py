class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        len_ax, len_com, len_by = len(A), len(B), len(B[0])
        result = [[0] * len_by for i in range(len_ax)]
        col_nzero_rows = {}
        for i in range(len_by):
            col_nzero_rows[i] = []
            for j in range(len_com):
                # j for row in B
                if B[j][i] != 0:
                    col_nzero_rows[i].append(j)
        
        print(col_nzero_rows)
        # B's row in this col_nzero_rows = A's col
                    
        for i in range(len_ax):
            for j in range(len_by):
                for k in col_nzero_rows[j]:
                    if A[i][k] != 0:
                        print(i, j, A[i][k] * B[k][j])
                        result[i][j] += A[i][k] * B[k][j]
                        
        return result
