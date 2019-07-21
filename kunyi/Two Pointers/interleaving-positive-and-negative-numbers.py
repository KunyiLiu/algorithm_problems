class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # negative to the first part, positive to the latter part, 
        # negative = 0, positive = 1 
        # if count_positive >= len(A) // 2 + 1,
        # negative = 1, positive = 0 
        # O(n^2) time, not much memory
        if A is None or len(A) == 0:
            return []
        
        stored_ind = 0 
        lenA = len(A)
        for i in range(lenA):
            if A[i] < 0:
                A[i], A[stored_ind] = A[stored_ind], A[i]
                stored_ind += 1 
        # stored_ind - can represent count of negative numbers
        if stored_ind >= lenA // 2 + 1:
            neg_ind, pos_ind = 0, 1 
        else:
            neg_ind, pos_ind = 1, 0 
            
        while neg_ind < lenA and pos_ind < lenA:
            while neg_ind < lenA and A[neg_ind] < 0:
                neg_ind += 2 
                
            while pos_ind < lenA and A[pos_ind] > 0:
                pos_ind += 2 
                
            if neg_ind < lenA and pos_ind < lenA:
                A[neg_ind], A[pos_ind] = A[pos_ind], A[neg_ind]
                
        return A
