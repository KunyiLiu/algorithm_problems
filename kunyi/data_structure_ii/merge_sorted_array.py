class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # 分析:涉及两个有序数组合并,设置i和j双指针,分别从两个数组的尾部想头部移动,
        # 并判断A[i]和B[j]的大小关系,从而保证最终数组有序##,同时每次index从尾部向头部移动
            
        i, j = m - 1, n - 1 
        pos = m + n - 1 
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[pos] = A[i]
                i -= 1 
                pos -= 1 
            else:
                A[pos] = B[j]
                j -= 1 
                pos -= 1 
                
        # while i >= 0:
        #     A[pos] = A[i]
        #     i -= 1 
        #     pos -= 1 
            
        while j >= 0:
            A[pos] = B[j]
            j -= 1 
            pos -= 1 
            
        return A
