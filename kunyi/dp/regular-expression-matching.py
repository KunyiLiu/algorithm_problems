class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # matching problem 
        # def: dp[m][n] - ifmatch between s[0...m-1] and p[0...n-1]
        # initial: dp[0][0] = True, 
        # reference: dp[i][j] = dp[i-1][j-1] if s[i-1] == p[j-1] or '.'
        # if p[j-1] == '*', like 'b*', it can be thought of '', dp[i][j] = dp[i][j-2]
        #                   else like s: abddd, p: abd*, s'last_elem == p's elem before '*'
        #                   dp[i][j] = dp[i-1][j]
        # result: dp[m][n]
        
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[0][0] = True 
        
        for i in range(1, n+1):
            if p[i-1] == '*' and i > 1:
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if self.is_char_match(s[i-1], p[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*' and j > 1:
                    dp[i][j] = dp[i][j-2]
                    if self.is_char_match(s[i-1], p[j-2]):
                        dp[i][j] |= dp[i-1][j]
                        
        return dp[m][n]
        
    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '.'
