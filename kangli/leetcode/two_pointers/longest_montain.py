class Solution(object):
    def longestMountain(self, A):
        ans = 0
        up_length, down_length = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                up_length[i] = up_length[i - 1] + 1
        for j in range(len(A) - 2, -1, -1):
            if A[j] > A[j + 1]:
                down_length[j] = down_length[j + 1] + 1
        for u, d in zip(down_length, up_length):
            if u and d:
                ans = max(ans, u + d + 1)
        return ans


'''
Submission Result: Accepted 
Next challenges: Remove Duplicates from Sorted Array IICandy CrushSubarrays with K Different Integers

72 / 72 test cases passed.
Status: Accepted
Runtime: 160 ms
Memory Usage: 13.6 MB
'''
