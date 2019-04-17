class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # dp[i] - the steps we need to enter i 
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            if i > 1:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
            
        return dp[n]
