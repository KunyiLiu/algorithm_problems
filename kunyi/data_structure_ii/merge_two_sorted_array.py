class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        i, j = 0, 0 
        result = []
        while i < m and j < n:
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1 
            else:
                result.append(B[j])
                j += 1 
                
        if i < m:
            result.extend(A[i:])
        
        if j < n:
            result.extend(B[j:])
            
        return result 
