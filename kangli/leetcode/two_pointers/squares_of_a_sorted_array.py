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
