class Solution:
    def commonChars(self, A):
        d, delete = {}, []
        res = []
        for c in A[0]:
            d[c] = 1 if c not in d else d[c]+1
        for word in A[1:]:
            for k, v in d.items():
                if k not in list(word):
                    delete.append(k)
                    continue
                elif word.count(k) < v:
                    d[k] = word.count(k)
        for c in delete:
            if c in d:
                del d[c]
        for k, v in d.items():
            while v > 0:
                res.append(k)
                v -= 1
        return res
'''
83 / 83 test cases passed.
Status: Accepted
Runtime: 96 ms
Memory Usage: 13.1 MB

Related Topics: Array, Hash Table
Similar Questions: Intersection of Two Arrays II
'''
