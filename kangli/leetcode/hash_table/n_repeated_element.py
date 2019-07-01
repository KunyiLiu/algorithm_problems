class Solution:
    def repeatedNTimes(self, A):
        n = len(A)/2
        d = {}
        for c in A:
            d[c] = 1 if c not in d else d[c]+1
        for k, v in d.items():
            if v == n:
                return k

'''
Success
Details
Runtime: 60 ms, faster than 42.14% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 14.2 MB, less than 48.00% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Next challenges:
Distribute Candies
Design HashSet
Longest Duplicate Substring

Related Topics: Hash Table
'''
