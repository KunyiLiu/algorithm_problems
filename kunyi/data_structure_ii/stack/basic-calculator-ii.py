class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        result, s = 0, s.strip()
        if s == '' or s is None:
            return result 
            
        stack = []
        ind = 0
        while ind < len(s):
            if s[ind] in ['+', '-', '*', '/']:
                stack.append(s[ind])
            elif s[ind] != ' ':
                if len(stack) == 0 or stack[-1] in ['+', '-', '*', '/']:
                    stack.append(int(s[ind]))
                else:
                    tmp = stack.pop() * 10 + int(s[ind])
                    stack.append(tmp)
            
            ind += 1 
        
        ind, stack_only = 0, []
        while ind < len(stack):
            if stack[ind] in ['*', '/']:
                tmp = stack_only.pop() * stack[ind+1] if stack[ind] == '*' else stack_only.pop() // stack[ind+1]
                stack_only.append(tmp)
                ind += 1 
            else:
                stack_only.append(stack[ind])
                
            ind += 1 
        while len(stack_only) > 0:
            # 3 + 4 - 5 * 5 + 55
            # 3 + 4 - 5 * 5   55 
            # 3 + 4 - 25  55 
            # 4/2 * 2 
            tmp = stack_only.pop()
            if len(stack_only) > 0:
                if stack_only[-1] in ['+', '-']:
                    operator = stack_only.pop()
                    result = result + tmp if operator == '+' else result - tmp
            else:
                result += tmp
            
        return result 
            
