class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        res = strs[0]
        for i in range(1, len(strs)):
            res = self.compare(res, strs[i])
            if not res:
                return ""
        return res

    def compare(self, str1, str2):
        start1, start2 = 0, 0
        while start1 < len(str1) and start2 < len(str2):
            if str1[start1] != str2[start2]:
                break
            start1 += 1
            start2 += 1
        return str1[:start1]


'''
Success
Details
Runtime: 56 ms, faster than 7.08% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 5.45% of Python3 online submissions for Longest Common Prefix.
Next challenges: Expressive Words, Buddy Strings, Parsing A Boolean Expression
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        pre = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(pre) != 0:
                pre = pre[0 : len(pre)-1]
                if pre == '':
                    return ''
        return pre


'''
Success
Details 
Runtime: 40 ms, faster than 71.24% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.8 MB, less than 5.45% of Python3 online submissions for Longest Common Prefix.
'''
