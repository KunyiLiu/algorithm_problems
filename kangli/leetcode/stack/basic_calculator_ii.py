class Solution:
    def calculate(self, s):
        if not s:
            return "0"
        sign, cur_num, stack = '+', 0, []
        s = s + " "
        for i, c in enumerate(s):
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            else:
                if c != ' ' or i == len(s) - 1:
                    if sign == '+':
                        stack.append(cur_num)
                    elif sign == '-':
                        stack.append(-cur_num)
                    elif sign == '*':
                        stack.append(stack.pop() * cur_num)
                    else:
                        stack.append(int(stack.pop() / cur_num))
                    sign = c
                    cur_num = 0
        return sum(stack)


'''
Success
Details
Runtime: 96 ms, faster than 83.67% of Python3 online submissions for Basic Calculator II.
Memory Usage: 15.8 MB, less than 16.82% of Python3 online submissions for Basic Calculator II.
Next challenges: Basic Calculator, Expression Add Operators, Basic Calculator III
'''
