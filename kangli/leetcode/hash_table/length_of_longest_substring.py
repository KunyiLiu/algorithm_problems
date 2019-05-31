class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j, length = 0, 0, 1
        window ={}
        while i < len(s) and j < len(s):
            if s[j] not in window:
                window[s[j]] = j
                length = max(len(window), length)
                j += 1
            else:
                i = window[s[j]] + 1
                j = window[s[j]] + 1
                window = {}
        return length
'''
Success
Details 
Runtime: 1184 ms, faster than 5.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.3 MB, less than 52.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
Next challenges:
Longest Substring with At Most Two Distinct Characters
Longest Substring with At Most K Distinct Characters
Subarrays with K Different Integers
'''
