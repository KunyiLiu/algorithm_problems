class Solution:
    def integerBreak(self, n: int) -> int:
        # break k => generate a dp[n] -> the max product for breaking nums
        # base: dp[2] = 1 (1* 1), dp[3] = 2 (1 * 2);
        # Two options: A. split k, and i - k; B. split k, then continue splitting i - k
        # inference: dp[i] = max(dp[i-k] * k, (i - k) * k) (k >= 2, i - K >= 2) 
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            for k in range(1, i):
                dp[i] = max(dp[i], dp[i-k] * k, (i - k) * k)

        return dp[n]

        
