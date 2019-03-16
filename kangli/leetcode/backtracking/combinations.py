class Solution(object):
    def combine(self, n, k):
        res = []
        self.build(res, [], 1, n, k)
        return res
    def build(self, res, cur, start, n, k):
        if k == 0:
            res.append(cur[:])
            return
        for i in range(start, n+1):
            cur.append(i)
            self.build(res, cur, i+1, n, k-1)
            cur.pop()
