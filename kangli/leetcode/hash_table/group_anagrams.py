class Solution(object):
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for s in strs:
            k = "".join(sorted(s))
            groups[k].append(s)
        res = []
        for g in groups:
            res.append(groups[g])
        return res
