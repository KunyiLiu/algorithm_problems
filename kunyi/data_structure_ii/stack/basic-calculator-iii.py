class Solution:
    """
    @param s: the expression string
    @return: the answer
    """
    def calculate(self, s):
        # Write your code here
        self.ind = 0
        return self.helper(s)
        
    def helper(self, s):
        stack, sign = [], '+'
        s = s.strip()
        # exit is sign != ')' not s[self.ind] != ')'
        while self.ind < len(s) and sign != ')':
            if s[self.ind] == ' ':
                self.ind += 1 
                continue
            
            # generate num 
            if s[self.ind] == '(':
                self.ind += 1
                num = self.helper(s)
            else:
                num = 0 
                while self.ind < len(s) and s[self.ind].isdigit():
                    num = num * 10 + int(s[self.ind])
                    self.ind += 1
            
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] *= num
            elif sign == '/':
                stack[-1] /= num
                
            if self.ind >= len(s):
                break

            sign = s[self.ind] 
            self.ind += 1 
            
        return sum(stack)

# nested function

class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        global_start = 0
        
        # create a recurssion + stack. helper(start, s) -> return result; new stack every time hitting (
        def helper(s):
            nonlocal global_start
            stack = []
            num, sign = 0, "+"

            while global_start < len(s) and s[global_start] != ")":
                if s[global_start].isspace():
                    global_start += 1
                    continue 

                if s[global_start] == "(":
                    global_start += 1
                    num = helper(s)
                else:
                    num = 0
                    while global_start < len(s) and s[global_start].isdigit():
                        num = num * 10 + int(s[global_start])
                        global_start += 1

                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    last = stack.pop()
                    stack.append(last * num)
                elif sign == "/":
                    last = stack.pop()
                    stack.append(int(last / num))
                
                if global_start >= len(s):
                    break

                if s[global_start] == ")":
                    global_start += 1
                    return sum(stack)

                sign = s[global_start]
                global_start += 1

            return sum(stack)

        return helper(s)
