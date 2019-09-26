class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # dp[i] - if [0, .. i-1] can be seperated to words in dict 
        # dp[i - len(w) - 1] is True, s[(i - len(w)): i] is True -> Tru
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 
        for i in range(1, n + 1):
            for word in dict:
                # s:  i - len(word) ... i - 1 
                if i >= len(word) and s[i - len(word) : i] == word and dp[i - len(word)]:
                    dp[i] = True 
                    
        return dp[n]
