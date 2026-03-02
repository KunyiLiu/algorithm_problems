class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # i as the pointer of s1, while j is the pointer of s2,
        # i + j would be the pointer of s3. 
        # dp[i][j] -> can it constusts the i + j part of s3
        # for the interleaving concept -> 
        # It only allows picking the next character from either string.
        # Consecutive picks from the same string naturally form a single substring.
        # Switching between strings automatically enforces alternating chunks.
        # Therefore |n - m| ≤ 1 is inherently guaranteed.
        # Time/Space: O(m * n)

        n = len(s1)
        m = len(s2)
        if n + m != len(s3):
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i >= 1 and s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True


                if j >= 1 and s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        
        return dp[n][m]




        
        
