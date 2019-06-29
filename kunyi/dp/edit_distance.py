class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # def: dp[i][j] #steps need to match w1[0...i-1] and w2[0...j-1]
        # initial: dp[0][j] = j, dp[i][0] = i (note: dp[0][0] = 0 imagine there is a '' preceding)
        # inference: dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1 if w1[i-1] != w2[j-1] else 0)
        # result: dp[n][m]
        # time O(mn) space O(mn)
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i 
            
        for j in range(m+1):
            dp[0][j] = j 
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (word1[i-1] != word2[j-1]))
                
        return dp[n][m]
    
    
##### improve space, only related to two rows when doing inference, => use rolling arrays #######
    def minDistance(self, word1, word2):
                n, m = len(word1), len(word2)
        dp = [[0] * (m+1), [0] * (m+1)]
        # for i in range(n+1):
        #     dp[i%2][0] = i 
            
        for j in range(m+1):
            dp[0][j] = j 
            
        for i in range(1, n+1):
            # error 
            dp[i%2][0] = i 
            for j in range(1, m+1):
                dp[i%2][j] = min(dp[(i-1)%2][j] + 1, dp[i%2][j-1] + 1, dp[(i-1)%2][j-1] + (word1[i-1] != word2[j-1]))
                
        return dp[n%2][m]

