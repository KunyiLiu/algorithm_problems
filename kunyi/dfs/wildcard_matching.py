class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # source substring starting form s_index matches to 
        # the pattern substring starting from p_index
        return self.is_match_helper(s, 0, p, 0, {})
        
    def is_match_helper(self, source, s_index, pattern, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        
        # exit
        # if remaining source is empty
        if len(source) == s_index:
            for i in range(p_index, len(pattern)):
                # can translate to empty string
                if pattern[i] != '*':
                    return False
            return True 
        
        # if remaining pattern is empty   
        if len(pattern) == p_index:
            return False 
            
        if pattern[p_index] != '*':
            matched = self.is_match_char(source[s_index], pattern[p_index]) and self.is_match_helper(source, s_index + 1, pattern, p_index + 1, memo)
        else:
            matched = self.is_match_helper(source, s_index, pattern, p_index + 1, memo) or self.is_match_helper(source, s_index + 1, pattern, p_index, memo)
            
        memo[(s_index, p_index)] = matched
            
        return matched
    
# method 2 DP bottom up
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        # [[False] * (n+1) for j in range(m+1)]
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(n+1):
                if i> 0 and j>0:
                    dp[i][j] |= dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] in ['*', '?'])
                if j>0:
                    dp[i][j] |= dp[i][j-1] and p[j-1] == '*'
                if i>0 and j>0:
                    dp[i][j] |= dp[i-1][j] and p[j-1] == '*'
                    
        return dp[m][n]
