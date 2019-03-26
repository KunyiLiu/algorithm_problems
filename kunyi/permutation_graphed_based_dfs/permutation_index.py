class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # from right to left
        # #smaller than preceding nubers * # permutations
        if A is None or len(A) == 0:
            return -1 
        n = len(A)
        permutation = 1
        result = 0
        for i in range(n-2, -1, -1):
            small = 0
            for j in range(i+1, n):
                if A[j] < A[i]:
                    small += 1
            
            result += small * permutation
            permutation *= (n - i)
            
        return result + 1
