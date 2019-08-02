class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = [None]*len(A)
        i, j = 0, len(A)-1
        k = len(A)-1
        while i <= j:
            if abs(A[i]) >= A[j]:
                res[k] = A[i]**2
                i += 1 
                k -= 1
            else:
                res[k] = A[j]**2
                j -= 1
                k -= 1
        return res
        

'''
Success
Details 
Runtime: 268 ms, faster than 52.97% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.7 MB, less than 5.10% of Python3 online submissions for Squares of a Sorted Array.
Next challenges: Sort Transformed Array

Related Topics: Array, Two Pointers
Similar Questions: Merge Sorted Array, Sort Transformed Array
'''


class Solution:
    def sortedSquares(self, A):
        i, j = 0, len(A) - 1
        res = [0] * len(A)
        pos = j
        while i <= j:
            if A[i] * A[i] >= A[j] * A[j]:
                res[pos] = A[i] * A[i]
                i += 1
                pos -= 1
            else:
                res[pos] = A[j] * A[j]
                j -= 1
                pos -= 1
        return res


'''
Submission Result: Accepted 
Next challenges: Merge Sorted Array, Sort Transformed Array
132 / 132 test cases passed.
Status: Accepted
Runtime: 164 ms
Memory Usage: 14.8 MB 
Your runtime beats 78.13 % of python3 submissions
Your memory usage beats 91.73 % of python3 submissions.

Related Topics: Array, Two Pointers
Similar Questions: Merge Sorted Array, Sort Transformed Array
'''
