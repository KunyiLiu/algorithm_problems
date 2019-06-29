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


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for w in strs:
            k = ''.join(sorted(w))
            d[k].append(w)
        res = []
        for v in d.values():
            res.append(v)
        return res


'''
Related Topics: Hash Table, String
Similar Questions: Valid Anagram, Group Shifted Strings

Success
Details 
Runtime: 108 ms, faster than 95.98% of Python3 online submissions for Group Anagrams.
Memory Usage: 16.1 MB, less than 53.87% of Python3 online submissions for Group Anagrams.
Next challenges:
Group Shifted Strings
'''
