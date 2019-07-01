class Solution:
    def findTheDifference(self, s, t):
        d, d1 = {}, {}
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1
        for c in t:
            d1[c] = 1 if c not in d1 else d1[c] + 1

        for k, v in d1.items():
            if k not in d:
                return k
            elif v != d[k]:
                return k

'''
Success
Details
Runtime: 40 ms, faster than 76.56% of Python3 online submissions for Find the Difference.
Memory Usage: 13.1 MB, less than 68.13% of Python3 online submissions for Find the Difference.
Next challenges:
Single Number

Related Topics: Hash Table, Bit Manipulation
Similar Questions: Single Number
'''
