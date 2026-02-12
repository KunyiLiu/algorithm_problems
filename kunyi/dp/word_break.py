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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dfs: from start, put "cats" and "cat" to the stack
        # once cats is popped from stack, check the next available words from the next ind,
        # put "in" to the stack, then put "car", but then no matched words from the remaining words, the ind havn't hit n

        # memo[i] - if s[i:] can be segmented.
        # time complexity: O(N * M * w), Space: O(N + M), N is the length of s, M is the wordDict number, w is the max length of words (slicing)
        n = len(s)
        wordDict = set(wordDict)
        # cache for start index → True/False
        memo = {}
        
        def dfs(start):
            if start >= n:
                return True
            
            if start in memo:
                return memo[start]

            for w in wordDict:
                if (start + len(w)) <= n and s[start: start + len(w)] == w:
                    if dfs(start + len(w)):
                        memo[start] = True
                        return True

            memo[start] = False
            return False

        result = dfs(0)
        return result


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = can segment s[i:]
        # base: dp[n] = True, inference: dp[i] = dp[i + len(w)] if w exist in wordDict
        # result: dp[0]
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]



