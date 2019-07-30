class Solution:
    def isValid(self, s: str) -> bool:
        stack, pairs = [], {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                close = stack.pop()
                if close != pairs[c]:
                    return False
        return True if len(stack) == 0 else False
                

'''
Success
Details 
Runtime: 36 ms, faster than 78.07% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14 MB, less than 5.00% of Python3 online submissions for Valid Parentheses.
Next challenges: Generate Parentheses, Longest Valid Parentheses, Remove Invalid Parentheses
Check If Word Is Valid After Substitutions
'''
