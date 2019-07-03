class Solution:
    def twoSumLessThanK(self, A, K):
        res = -1
        l, r = 0, len(A)-1
        A = sorted(A)
        while l < r:
            if A[l] + A[r] < K:
                res = max(res, A[l]+A[r])
                l += 1
            else:
                r -= 1
        return res


class Solution2:
    def twoSumLessThanK(self, A, K):
        res = []
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] + A[j] < K:
                    res.append(A[i]+A[j])
        return max(res) if res else -1

'''
Success (First Solution)
Details
Runtime: 36 ms, faster than 92.73% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 13.1 MB, less than 33.33% of Python3 online submissions for Two Sum Less Than K.

Success
Details
Runtime: 84 ms, faster than 30.80% of Python3 online submissions for Two Sum Less Than K.
Memory Usage: 13.2 MB, less than 33.33% of Python3 online submissions for Two Sum Less Than K.
Next challenges:
Two Sum
Two Sum II - Input array is sorted
3Sum Smaller

Related Topics: Array
Similar Questions: Two Sum, Two Sum II - Input array is sorted, 3Sum Smaller, Subarray Product Less Than K
Hints: 1) What if we have the array sorted?
2) Loop the array and get the value A[i] then we need to find a value A[j] such that A[i] + A[j] < K
which means A[j] < K - A[i]. In order to do that we can find that value with a binary search.
'''
