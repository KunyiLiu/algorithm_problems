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

############# O(n^2) Enum from mid point ########

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # Time complexity O(n^2)
        # expand the substring from the mid point 
        if not s:
            return ''
            
        self.start, self.longest = 0, 0 
        for mid in range(len(s)):
            # update self.start and self.longest
            self.helper(s, mid, mid)
            self.helper(s, mid, mid + 1)
            
        return s[self.start:(self.start + self.longest)]
        
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1 
            right += 1 
        local = right - 1 - (left + 1) + 1
        if self.longest < local:
            self.longest = local
            self.start = left + 1

############# O(n^2) dp #############
class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # dp[i][j] - is_pal substring between i to j  
        # dp[i][i] means the single char from string, True
        # dp[i][j] = (dp[i + 1][j-1] and s[i] == s[j]
        
        if not s:
            return ''
        
        len_s = len(s)
        dp = [[False] * len_s for i in range(len_s)]
        start, longest = 0, 1
        for i in range(len_s):
            dp[i][i] = True 
            
        for length in range(2, len_s + 1):
            for i in range(len_s - length + 1):
                j = i + length - 1 
                # start from 0, 1, 
                if i + 1 < j:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j]
                
                if dp[i][j] and length > longest:
                    start = i 
                    longest = length
        # start + longest - 1 - start + 1 = longest
        return s[start: (start + longest)]    
