class Solution:
    """
    @param A: an array
    @param B: an array
    @return: the minimum number of swaps to make both sequences strictly increasing
    """
    def minSwap(self, A, B):
        # cannot do greedy
        # have two lists to record the state swap = int[n] (choose to swap for i, non-swap
        # swap[0] = 1, swap[0] = 0, else max_int
        # inference:
        # 1. A[i] > A[i - 1] && B[i] > B[i - 1] or 
        # 2. A[i] > B[i - 1] && B[i] > A[i - 1]
        # if 1, non-swap[i] = min(non-swap[i-1], non-swap[i]); swap[i] = min(.., swap[i-1] + 1) continue swapping
        # if 2, non-swap[i] = min(non-swap[i], swap[i-1]), dont need to do swap 
        #       swap[i] = min(non-swap[i], non-swap[i-1] + 1)
        # notice it can occur at the same time 
        import sys
        max_int = sys.maxsize
        n = len(A)
        swap, non_swap = [max_int] * n, [max_int] * n 
        swap[0] = 1 
        non_swap[0] = 0
        
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                non_swap[i] = min(non_swap[i], non_swap[i-1])
                swap[i] = min(swap[i], swap[i-1] + 1) # now are actually condition 2 
            if A[i] > B[i-1] and B[i] > A[i-1]:
                non_swap[i] = min(non_swap[i], swap[i-1])
                swap[i] = min(swap[i], non_swap[i-1] + 1)
        
        print(swap, non_swap)        
        return min(swap[n-1], non_swap[n-1])
