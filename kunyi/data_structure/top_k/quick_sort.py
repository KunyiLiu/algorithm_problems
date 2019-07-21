class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # quick sort 
        # O(nlogn)
        if len(A) == 0:
            return A
        self.quick_sort(A, 0, len(A) - 1)
        return A 
        
    def quick_sort(self, A, start, end):
        if start == end:
            return 
        
        l, r = start, end 
        pivot = A[start]
        while l <= r:
            while l <= r and A[l] < pivot:
                l += 1 
            while l <= r and A[r] > pivot:
                r -= 1 
            if l <= r:
                A[l], A[r] = A[r], A[l]
                l += 1 
                r -= 1 
                
        self.quick_sort(A, start, l-1)
        self.quick_sort(A, l, end)
