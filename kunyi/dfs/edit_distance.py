class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        if word1 is None or word2 is None:
            return 0
        len1, len2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for i in range(len2)] for j in range(len1)]
        for i in range(len1):
            dp[i][0] = i
        for j in range(len2):
            dp[0][j] = j
        for i in range(1, len1):
            for j in range(1, len2):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + (word1[i-1] != word2[j-1]))
        return dp[-1][-1]
