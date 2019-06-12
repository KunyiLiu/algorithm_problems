#####################  O(n^3) ####################
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Time complexity O(n^3)
        if not s:
            return ''
            
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                j = i + length - 1 
                if self.is_palidrome(s, i, j):
                    return s[i: (j+1)]
                    
        return ''
        
    def is_palidrome(self, s, i, j):
        while i < j and s[i] == s[j]:
            i += 1 
            j -= 1 
        return i >= j
