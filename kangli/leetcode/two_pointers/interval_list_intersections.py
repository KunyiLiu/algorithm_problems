class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][1] and A[i][1] >= B[j][0]:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] > B[j][1]:
                j += 1 
            else:
                i += 1 
        return res


'''
Success
Details 
Runtime: 176 ms, faster than 53.45% of Python3 online submissions for Interval List Intersections.
Memory Usage: 14.5 MB, less than 5.08% of Python3 online submissions for Interval List Intersections.
Next challenges: Merge Intervals, Merge Sorted Array, Employee Free Time
'''
