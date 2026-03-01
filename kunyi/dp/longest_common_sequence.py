class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a matrix of n * m
        # dp[i][j] - represent the match between text1[:(i+1)] with text2[:{j+1)]
        # base: dp[i][0], loop over text1 to match with text2[0], dp[0][j]
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if not (text1[i] == text2[j])
        # else dp[i-1][j-1] + 1
        # result: dp[n-1][m-1]
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1,n):
            # the dp[i][0] should be at max 1
            dp[i][0] = max(dp[i-1][0], 1 if text1[i] == text2[0] else 0)

        for i in range(1, m):
            dp[0][i] = max(dp[0][i-1], 1 if text1[0] == text2[i] else 0)

        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j - 1])

        return dp[n-1][m-1]

#####  Cleaner: use padding ######
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
