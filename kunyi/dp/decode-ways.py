class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # definition: dp[i] - the number of decode ways of s(0...i-1) 
        # initial: dp[0] = 1, dp[1] if s[0] > 0 
        # inference: dp[i] = dp[i-2] if s[i-2, i-1] is valid + dp[i-1] if s[i-1]
        # result: dp[n]
        n = len(s)
        if n < 1:
            return 0
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1 if int(s[0]) > 0 else 0 
        for i in range(2, n+1):
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
                
        return dp[n]
