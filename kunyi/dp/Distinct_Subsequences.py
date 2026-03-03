class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i][j] = number of distinct subsequences of s[:i]
                   that equal t[:j]

        Dimensions:
            i -> first i characters of s  (0..n)
            j -> first j characters of t  (0..m)

        Base cases:
            dp[i][0] = 1
                An empty string t can always be formed from any prefix of s
                by deleting all characters.

            dp[0][j] = 0 for j > 0
                Non-empty t cannot be formed from empty s.

        Transition:
            If s[i-1] != t[j-1]:
                We must skip s[i-1]
                dp[i][j] = dp[i-1][j]

            If s[i-1] == t[j-1]:
                Two choices:
                    1) Skip s[i-1]  → dp[i-1][j]
                    2) Use s[i-1]   → dp[i-1][j-1]

                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

        Answer:
            dp[n][m]
        """

        n, m = len(s), len(t)

        # Edge case: impossible if t longer than s
        if m > n:
            return 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Empty t case
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Always inherit the "skip s[i-1]" option
                dp[i][j] = dp[i - 1][j]

                # If characters match, add the "use it" option
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[n][m]

###### 1D Dp #####
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        1D DP Optimization

        dp[j] = number of subsequences of processed prefix of s
                that equal t[:j]

        Iterate j backwards to avoid overwriting needed values.
        """

        n, m = len(s), len(t)
        if m > n:
            return 0

        dp = [0] * (m + 1)
        dp[0] = 1  # empty t

        for i in range(1, n + 1):
            # iterate backwards
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
