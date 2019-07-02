class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # def: dp[i][j] - if match between s[0...i-1], p[0...j-1]
        # initial: dp[0][0] = True, dp[0][j] = dp[0][j-1] if p[j-1] == '*' (empty)
        # inf: if match_char, dp[i][j] = dp[i-1][j-1]
        #  if '*', it can indicate '', dp[i][j] |= dp[i][j-1]
        #          it can indicate any char (ith char), dp[i][j] |= dp[i-1][j] (remain *)
        # result: dp[m][m]
        # time/space O(mn)
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[0][0] = True 
        for i in range(1, n + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                if self.is_char_match(s[i-1], p[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                    
        return dp[m][n]
        
    def is_char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'
