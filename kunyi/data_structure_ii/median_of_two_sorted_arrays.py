class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # A[k/2 -1] > B[k/2 - 1], kth not in B[:k/2] 
        # A[k/2 - 1] < B[k/2 - 1], kth not in A[:k/2]
        n = len(A) + len(B)
        if n % 2 == 1:
            result = self.findkthelement(A, B, n//2 + 1)
        else:
            small = self.findkthelement(A, B, n//2)
            big = self.findkthelement(A, B, n//2 + 1)
            result = (small + big) / 2.0 
            
        return result 
        
    def findkthelement(self, A, B, k):
        # exit
        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
            
        a = A[k// 2 - 1] if len(A) >= k// 2 else None
        b = B[k//2 - 1] if len(B) >= k//2 else None
        
        if b is None or (a is not None and b > a):
            result = self.findkthelement(A[k//2:], B, k - k//2)
        else:
            result = self.findkthelement(A, B[k//2:], k - k//2)
            
        return result 
        
  ################ two pointer for selecting kth element   #######
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # A[k/2 -1] > B[k/2 - 1], kth not in B[:k/2] 
        # A[k/2 - 1] < B[k/2 - 1], kth not in A[:k/2]
        n = len(A) + len(B)
        if n % 2 == 1:
            result = self.findkthelement(A, B, n//2 + 1)
        else:
            small = self.findkthelement(A, B, n//2)
            big = self.findkthelement(A, B, n//2 + 1)
            result = (small + big) / 2.0 
            
        return result 
        
    def findkthelement(self, A, B, k):
        # try using two pointers 
        p1, p2 = 0, 0 
        tmp = None
        while p1 < len(A) and p2 < len(B):
            if A[p1] <= B[p2]:
                tmp = A[p1]
                p1 += 1 
            else:
                tmp = B[p2]
                p2 += 1
            
            if p1 + p2 == k:
                return tmp 
                
        if p1 < len(A):
            return A[k - p2 - 1]
            
        if p2 < len(B):
            return B[k - p1 - 1]
