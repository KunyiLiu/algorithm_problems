class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        i, j = 0, 0
        res = 1
        unique = set()
        while i < len(s) and j < len(s):
            if s[j] not in unique:
                unique.add(s[j])
                j += 1
            else:
                unique = set()
                res = max(res, j - i)
                i += 1
                j = i
        res = max(res, j - i)
        return res


'''
Success
Details
Runtime: 908 ms, faster than 5.58% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.9 MB, less than 5.05% of Python3 online submissions for Longest Substring Without Repeating Characters.
Next challenges: Longest Substring with At Most Two Distinct Characters,
Longest Substring with At Most K Distinct Characters, Subarrays with K Different Integers
'''
