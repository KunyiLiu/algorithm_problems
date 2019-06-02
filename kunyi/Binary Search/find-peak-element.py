####### two standard #######
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # A can be represented as a list of ++--++--
        # the first would be +, while the last would be - 
        # find any ind that are +- 
        if  A is None or len(A) == 0:
            return -1 
            
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if mid > 0 and A[mid] < A[mid - 1]:
                end = mid 
            elif mid > 0:
                if A[mid] > A[mid + 1]:
                    return mid 
                else:
                    start = mid

        if start > 0 and A[start] > A[start - 1] and A[start] > A[start + 1]:
            return start 
        # if end < len(A) - 1 and A[end] > A[end - 1] and A[end] > A[end + 1]:
        #     return end 
        
        return -1
