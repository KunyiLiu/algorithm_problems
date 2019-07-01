class Solution:
    def firstUniqChar(self, s):
        d = {}
        for c in s:
            d[c] = 1 if c not in d else d[c] + 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


'''
Success
Details
Runtime: 140 ms, faster than 39.84% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 13.4 MB, less than 44.30% of Python3 online submissions for First Unique Character in a String.
Next challenges:
Sort Characters By Frequency

Related Topics: Hash Table, String
Similar Questions: Sort Characters By Frequency
'''
