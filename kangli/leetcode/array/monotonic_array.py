class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        increasing, decreasing = False, False
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                increasing = True
            if A[i] < A[i-1]:
                decreasing= True
        if increasing and decreasing:
            return False
        else:
            return True
    

'''
Success
Details 
Runtime: 600 ms, faster than 12.19% of Python3 online submissions for Monotonic Array.
Memory Usage: 19.6 MB, less than 5.26% of Python3 online submissions for Monotonic Array.
Next challenges: 4Sum, Missing Ranges, Array of Doubled Pairs
'''


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        elem, test = A[0], False
        for c in A[1:]:
            if c != elem:
                test = True
        if not test:
            return True
        increasing = A[0] < A[-1]
        if increasing:
            return self.test_increasing(A)
        else:
            return self.test_decreasing(A)
    
    def test_increasing(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                return False
        return True
    
    def test_decreasing(self, A):
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                return False
        return True
    

'''
Success
Details 
Runtime: 556 ms, faster than 63.68% of Python3 online submissions for Monotonic Array.
Memory Usage: 19.9 MB, less than 5.26% of Python3 online submissions for Monotonic Array.
Next challenges: 4Sum, Missing Ranges, Array of Doubled Pairs
'''
