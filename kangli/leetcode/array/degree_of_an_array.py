class Solution(object):
    def findShortestSubArray(self, nums):
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)
        deg = 0
        for k, v in d.items():
            if len(v) > deg:
                deg = len(v)
        min_length = len(nums)
        for v in d.values():
            if len(v) == deg:
                min_length = min(min_length, v[-1] - v[0] + 1)
        return min_length
