class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                x_d = p[0] - q[0]
                y_d = p[1] - q[1]
                dist = x_d * x_d + y_d * y_d
                cmap[dist] = 1 if dist not in cmap else cmap[dist] + 1
            for k in cmap:
                res += cmap[k] * (cmap[k] - 1)
        return res

'''
Success
Details 
Runtime: 716 ms, faster than 94.32% of Python3 online submissions for Number of Boomerangs.
Memory Usage: 13.2 MB, less than 89.62% of Python3 online submissions for Number of Boomerangs.
Next challenges:
Line Reflection

Related Topics: Hash Table
Similar Questions: Line Reflection
'''
