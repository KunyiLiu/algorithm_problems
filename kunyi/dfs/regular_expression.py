class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # dp[i][j] means if s[0-i] matches with p[0-j] (i, j not included)
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[0][0] = True 
        
        for i in range(n):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i-1]
        
        for i in range(m):
            for j in range(n):
                if self.is_char_match(s[i], p[j]):
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j-1]
                    # a char precede to * = s[i], see the last step of string s
                    if self.is_char_match(s[i], p[j-1]):
                        dp[i+1][j+1] |= dp[i][j+1]
                    
        return dp[m][n]
        
    def is_char_match(self, char_s, char_p):
        return char_p == char_s or char_p == '.'
