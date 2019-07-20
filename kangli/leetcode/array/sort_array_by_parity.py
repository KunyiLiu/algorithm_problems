class Solution:
    def sortArrayByParity(self, A):
        i, j = 0, len(A)-1
        while i < j:
            if A[i]%2 == 0 and A[j]%2 == 1:
                i += 1
                j -= 1
            elif A[i]%2 == 1 and A[j]%2 == 1:
                j -= 1
            elif A[i] %2 == 0 and A[j]%2 ==0:
                i+= 1
            else:
                A[i], A[j] = A[j], A[i]
                i +=1
                j -= 1
        return A


'''
Submission Result: Accepted
Next challenges: Minimum Path Sum, Construct Binary Tree from Inorder and Postorder Traversal,
Flip String to Monotone Increasing

285 / 285 test cases passed.
Status: Accepted
Runtime: 60 ms
Memory Usage: 13.8 MB
'''
