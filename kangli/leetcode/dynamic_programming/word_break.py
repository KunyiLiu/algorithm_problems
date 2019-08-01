class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                
                print(j, s[i:j+1])
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]
    

'''
Success
Details 
Runtime: 100 ms, faster than 5.70% of Python3 online submissions for Word Break.
Memory Usage: 14.2 MB, less than 5.33% of Python3 online submissions for Word Break.
Next challenges: Word Break II
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False for _ in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if s[i - len(w) + 1:i + 1] == w and (arr[i - len(w)] or i - len(w) == -1):
                    arr[i] = True
        return arr[-1]
'''
Success
Details 
Runtime: 44 ms, faster than 74.40% of Python3 online submissions for Word Break.
Memory Usage: 13.2 MB, less than 56.77% of Python3 online submissions for Word Break.
Next challenges:
Word Break II

Related Topics: Dynamic Programming
Similar Questions: Word Break II
'''
