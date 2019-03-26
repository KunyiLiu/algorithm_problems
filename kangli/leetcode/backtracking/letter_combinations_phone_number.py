class Solution(object):
    def letterCombinations(self, digits):

        numbers = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno",
                   '7': "pqrs", '8': "tuv", '9': "wxyz"}

        def permute(cur, next_digits):
            if len(next_digits) == 0:
                res.append(cur)
            else:
                for l in numbers[next_digits[0]]:
                    permute(cur + l, next_digits[1:])

        res = []
        if not digits: return res
        permute("", digits)
        return res

'''
Success
Details 
Runtime: 32 ms, faster than 9.99% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 11.9 MB, less than 5.15% of Python online submissions for Letter Combinations of a Phone Number.
Next challenges:
Binary Watch

related topics: String, Backtracking
Similar questions: Generate Parentheses, Combination Sum, Binary Watch
'''
