class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # combine with find minimum with rotated sorted array 
        # partition A to A[:ind] and A[ind:]
        # compare the target with last element to see we should do the
        # second binary search with the first part or latter one 
        if A is None or len(A) == 0:
            return -1 
        
        start, end = 0, len(A) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if A[mid] == target:
                return mid 
            elif A[mid] > target:
                if A[mid] > A[-1]:
                    if target < A[-1]:
                        start = mid 
                    elif target == A[-1]:
                        return len(A) - 1 
                    else:
                        end = mid 
                else:
                    end = mid
            else:
                if A[mid] <= A[-1]:
                    if target < A[-1]:
                        start = mid 
                    elif target == A[-1]:
                        return len(A) - 1 
                    else:
                        end = mid 
                else:
                    start = mid 
                    
        if A[start] == target:
            return start
        elif A[end] == target:
            return end 
            
        return -1
        
###### less level #######
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        start=0
        end=len(A)-1
        if A==[] or A==None:
            return -1
        k=A[end]

        while start + 1 < end:
            mid = start + (end - start)//2
            if A[start] > A[mid]:
                if target <= A[start] and target < A[mid]:
                    end = mid
                elif target <= A[start] and target >= A[mid]:
                    start = mid
                else:
                    end = mid
            else:
                if target >= A[start] and target < A[mid]:
                    end = mid
                elif target >= A[start] and target >= A[mid]:
                    start = mid
                else:
                    start = mid
        if A[start]==target:
            return start
        elif A[end]==target:
            return end
        else:
            return -1
