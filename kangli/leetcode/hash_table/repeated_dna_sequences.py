class Solution:
    def findRepeatedDnaSequences(self, s):
        d = {}
        res = []
        for i in range(len(s) - 9):
            d[s[i:i + 10]] = 1 if s[i:i + 10] not in d else d[s[i:i + 10]] + 1

        for k, v in d.items():
            if v > 1:
                res.append(k)
        return res


'''
Related Topics: Hash Table, Bit Manipulation

Success
Details
Runtime: 76 ms, faster than 53.45% of Python3 online submissions for Repeated DNA Sequences.
Memory Usage: 26.7 MB, less than 11.36% of Python3 online submissions for Repeated DNA Sequences.
Next challenges:
Valid Sudoku
Isomorphic Strings
Top K Frequent Elements
'''
