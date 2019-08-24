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
