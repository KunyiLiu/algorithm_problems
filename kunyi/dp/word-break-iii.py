class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # dp[i][j] - # break for s[i...j], i,j included
        # initial: dp[i][i] - if s[i] in dict, else 0
        # inference: dp[i][j] +=  dp[i][m] * 1 if s[m+1:(j+1)])
        # dp[0][n-1]
        n = len(s)
        dp = [[0]* n for i in range(n)]
        
        new_dict = set()
        for d in dict:
            new_dict.add(d.lower())
            
        for i in range(n):
            for j in range(i, n):
                if (s[i:(j+1)]).lower() in new_dict:
                    dp[i][j] = 1 
                    
        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    # dp[i][k] can dp[i][i] .. dp[i][j-1]
                    dp[i][j] += dp[i][k] * dp[k+1][j]
                    
        return dp[0][n-1]
