class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # Remember heap is a complete tree 
        # we should start from the lowest level heap (like the 1 as parent)
        
        for i in range((len(A) -1)/2, -1, -1):
            self.shiftdown(A, i)
            
    def shiftdown(self, A, ind):
        while ind * 2 + 1 < len(A):
            # select the smallest one
            son_ind = ind*2 + 1
            if son_ind + 1 < len(A) and A[son_ind + 1] < A[son_ind]:
                son_ind += 1 
                
            if A[son_ind] > A[ind]:
                break 
            
            A[son_ind], A[ind] = A[ind], A[son_ind]
            ind = son_ind
