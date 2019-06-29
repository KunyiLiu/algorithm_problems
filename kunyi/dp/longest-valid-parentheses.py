class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # def: dp[i] - # consecutive valid pairs from 0 to i in s
        # initial: dp[i] = 0 
        # inference: if s[i] is (, stack; if s[i] is ), add 2 to the dp[i-1]
        # and check to see if we shall add the length of the valid substring just before the term (( .. ))
        stack = []
        n = len(s)
        if n == 0:
            return 0
        result = [0] * n
        for i in range(len(s)):
            if len(stack) > 0:
                # peek = stack[-1]
                if s[i] == ')':
                    matching_ind = stack.pop()
                    if matching_ind >= 1:
                        result[i] = result[i-1] + 2 + result[matching_ind - 1]  
                    else:
                        result[i] = result[i-1] + 2
            if s[i] == '(':
                stack.append(i)
                
        return max(result)
