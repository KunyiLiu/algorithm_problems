class Solution:
    def largestSumAfterKNegations(self, A, K):
        min_pos = (100, 0)
        negatives = []
        for i, n in enumerate(A):
            if n < 0:
                negatives.append((n, i))
            if n >=0 and n < min_pos[0]:
                min_pos = (n, i)
        negatives = sorted(negatives, key=lambda x:x[0])
        if K >= len(negatives):
            for p in negatives:
                A[p[1]] = -A[p[1]]
            K -= len(negatives)
        else:
            for i in range(K):
                A[negatives[i][1]]= -A[negatives[i][1]]
            K = 0
        effect =  -1 if K%2 else 1
        for i, n in enumerate(A):
            if n >= 0 and n < min_pos[0]:
                min_pos = (n, i)
        A[min_pos[1]] = effect*A[min_pos[1]]
        return sum(A)
    
        
'''
Success
Details 
Runtime: 28 ms, faster than 99.46% of Python3 online submissions for Maximize Sum Of Array After K Negations.
Memory Usage: 13.4 MB, less than 5.06% of Python3 online submissions for Maximize Sum Of Array After K Negations.
Next challenges:
Queue Reconstruction by Height
Employee Free Time
Minimum Number of K Consecutive Bit Flips

Related Topics: Greedy
'''
