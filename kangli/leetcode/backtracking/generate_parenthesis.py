class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, "", res)
        return res 
    
    def helper(self, l, r, temp, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(temp)
            return 
        if l > 0:
            self.helper(l-1, r, temp+"(", res)
        if r > 0:
            self.helper(l, r-1, temp+")", res)


'''
Success
Details 
Runtime: 44 ms, faster than 49.70% of Python3 online submissions for Generate Parentheses.
Memory Usage: 13.8 MB, less than 5.11% of Python3 online submissions for Generate Parentheses.
Next challenges: Letter Combinations of a Phone Number

Related Topics: String, Backtracking
Similar Questions: Letter Combinations of a Phone Number, Valid Parentheses
'''
