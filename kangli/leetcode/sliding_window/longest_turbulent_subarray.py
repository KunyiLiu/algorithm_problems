class Solution:
    def maxTurbulenceSize(self, A):
        if len(A) == 1:
            return len(A)
        if len(A) == 2:
            return len(A) if A[0] != A[1] else 1
        i, j, k = 0, 1, 2
        res = A[0] < A[1]
        length = 1
        while k < len(A):
            temp = A[j] < A[k]
            if res == temp or A[j] == A[k]:
                i = j
                if A[j] == A[k]:
                    i = k
                j += 1
                k += 1
            else:
                res = A[j] < A[k]
                j +=1
                k +=1
                length = max(length, j-i+1)
        length = max(length, j-i+1)
        return length


'''
Success
Details
Runtime: 576 ms, faster than 64.29% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 18.2 MB, less than 6.49% of Python3 online submissions for Longest Turbulent Subarray.
Next challenges: Maximum Subarray
'''
