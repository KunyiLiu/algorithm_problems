class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # if meet ' ' continue 
        # meet digit, num = num * 10 + digit 
        # (all the remainning will reset num )
        # mmet '+', '-', append +/- num to stack 
        # meet '(', append current operator, append '('
        # meet ')', pop until meet '(', and pop operator, append sub result to stack 
        num, operator = 0, '+'
        stack = []
        s = s.strip()
        for i, char in enumerate(s):
            if char.isnumeric():
                num = num * 10 + int(char)
            if char in ['+', '-']:
                if operator == '+':
                    stack.append(num)
                if operator == '-':
                    stack.append(-num)
                operator = char 
                num = 0 
            elif char == '(':
                stack.append(operator)
                stack.append('(')
                # ERROR - update operator
                operator = '+'
            elif char == ')':
                tmp = num if operator == '+' else -num
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack.pop()
                operator = stack.pop()
                if operator == '+':
                    stack.append(tmp)
                elif operator == '-':
                    stack.append(-tmp)
                num = 0 
            elif i == len(s) - 1:
                stack.append(num if operator == '+' else -num)
                    
        return sum(stack)
        
        
####################### result, number, sign, stack
    def calculate(self, s):
        stack = []
        result = 0
        number = 0
        sign = 1
        for c in s:
            if c in '1234567890':
                number = number * 10 + int(c)
            elif c == '+':
                result += sign * number
                number = 0 
                sign = 1 
            elif c == '-':
                result += sign * number
                number = 0 
                sign = -1 
            elif c == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0 
                result *= stack[-1]
                result += stack[-2]
                stack = stack[:-2]
        result += sign * number
        return result
