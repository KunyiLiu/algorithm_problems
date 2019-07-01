class Solution:
    def canPermutePalindrome(self, s):
        counts = {}
        for c in s:
            counts[c] = 1 if c not in counts else counts[c] + 1
        odd = 0
        for k, v in counts.items():
            if v % 2 != 0:
                odd += 1
        return True if odd <= 1 else False


'''
Success
Details
Runtime: 32 ms, faster than 91.17% of Python3 online submissions for Palindrome Permutation.
Memory Usage: 13.1 MB, less than 72.81% of Python3 online submissions for Palindrome Permutation.
Next challenges:
Longest Palindromic Substring
Valid Anagram
Palindrome Permutation II
Longest Palindrome
'''
