class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # find the first and last position 
        if A is None or len(A) == 0:
            return [-1, -1]
            
        n = len(A)
        # first element of target in A
        start_ind = self.binary_search_first(A, target, 0, n - 1)
        if start_ind == -1:
            return [-1, -1]
        end_ind = self.binary_search_last(A, target, start_ind + 1, n -1)
        return [start_ind, end_ind]
        
    def binary_search_first(self, array, target, left, right):
        start, end = left, right
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if array[mid] >= target:
                end = mid 
            else:
                start = mid 
                
        if array[start] == target:
            return start 
        if array[end] == target:
            return end 
        
        return -1
        
    def binary_search_last(self, array, target, left, right):
        start, end = left, right
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if array[mid] <= target:
                start = mid 
            else:
                end = mid 
                
        if array[end] == target:
            return end 
        if array[start] == target:
            return start
        
        return -1
