class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        stored_ind = 0 
        for i in range(len(A)):
            if A[i] != elem:
                A[stored_ind] = A[i]
                stored_ind += 1 
                
        return stored_ind
