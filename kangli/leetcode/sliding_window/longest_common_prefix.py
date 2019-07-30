class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            if i == 0:
                pref = self.get_prefix(strs[i], strs[i+1])
            else:
                pref = self.get_prefix(pref, strs[i])
        return pref
            
    def get_prefix(self, s1, s2):
        pref = []
        if not s1 or not s2:
            return ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                pref.append(s1[i])
            else:
                break
        return "".join(pref)
            
        
'''
Success
Details 
Runtime: 48 ms, faster than 21.67% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14 MB, less than 5.41% of Python3 online submissions for Longest Common Prefix.
Next challenges: Longest Substring with At Most Two Distinct Characters, Count Different Palindromic Subsequences, 
Find And Replace in String
'''


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
'''
Success
Details 
Runtime: 52 ms, faster than 14.97% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 5.41% of Python3 online submissions for Longest Common Prefix.
Next challenges: Multiply Strings, Special Binary String, Longest Repeating Substring
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
