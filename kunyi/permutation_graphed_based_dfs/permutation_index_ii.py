class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0 
        
        counter = {}    
        sub_perm, multi_fact,index = 1, 1, 1 
        for i in range(len(A) - 1, -1, -1):
            if A[i] not in counter:
                counter[A[i]] = 0 
                
            counter[A[i]] += 1 
            multi_fact *= counter[A[i]] 
            smaller = 0 
            # the num before this permutation, which would be smaller 
            for j in range(i+1, len(A)):
                if A[j] < A[i]: 
                    smaller += 1 
                    
            index += smaller * sub_perm / multi_fact
            sub_perm *= (len(A) - i) 
            
        return index 
