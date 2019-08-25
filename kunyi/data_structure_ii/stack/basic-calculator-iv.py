#   m - eval, n - expression(variables + symbols)
###### space: O(m+n), time complexity: O(2**n + m)
from collections import Counter 

class Poly(Counter):
    def __add__(self, others):
        self.update(others)
        return self 
        
    def __sub__(self, others):
        self.update({k: -v for k, v in others.items()})
        return self
        
    def __mul__(self, others):
        ans = Poly()
        for k1, v1 in self.items():
            for k2, v2 in others.items():
                ans.update({tuple(sorted(k1 + k2)): v1*v2})
                
        return ans 
                

class Solution:
    """
    @param expression: the given expression
    @param evalvars: the key of the evaluation map
    @param evalints: the value of the evaluation map
    @return: a list of tokens representing the simplified expression
    """
    def basicCalculatorIV(self, expression, evalvars, evalints):
        #  the difficulty is in how to handle the constants and variables 
        # use a Counter to deal with it, 8 -> () = 8, a -> (a, ) = 1 (term tuple: coefficient)
        # def parse
        # first we convert the expression to two lists bucket (a list of term pair) and symbols 
        #       if encounter ( or ), we extract that out and parse it recursively 
        # then combine to deal with the operation and return a whole counter 
        # evaluate 
        #       replace the variables with values 
        # then list by degree, lexicographic, coefficient 
        eval_map = dict()
        for var, ints in zip(evalvars, evalints):
            eval_map[var] = ints 
            
        ans_poly = self.parse(expression)
        new_ans = Poly()
        for term_tup, val in ans_poly.items():
            new_tup = []
            for token in term_tup:
                if token in eval_map:
                    val *= eval_map[token]
                else:
                    new_tup.append(token)
                
            new_ans[tuple(new_tup)] += val 
        
        # print(new_ans, ans_poly)  
        result = sorted(new_ans.items(), key=lambda x: (-len(x[0]), x[0], x[1]))
        return ["*".join((str(v),) + k) for k, v in result if v]
            
    
    def parse(self, expression):
        """
        expression -> a whole counter 
        """
        buckets, symbols = [], []
        ind = 0 
        while ind < len(expression):
            # priority backet first
            # Error 
            if expression[ind] == '(':
                bal = 1
                for j in range(ind+1, len(expression)):
                    if expression[j] == '(': bal += 1 
                    if expression[j] == ')': bal -= 1 
                    if bal == 0:
                        break
                part_term = self.parse(expression[ind+1:j])
                buckets.append(part_term)
                ind = j 
            # alphanumeric
            elif expression[ind].isalnum():
                poly = Poly()
                if expression[ind].isalpha():
                    num = []
                    while ind < len(expression) and expression[ind].isalpha():
                        num.append(expression[ind])
                        ind += 1 
                    ind -= 1 
                    poly[(''.join(num), )] += 1
                else:
                    num = 0 
                    while ind < len(expression) and expression[ind].isdigit():
                        num = num * 10 + int(expression[ind])
                        ind += 1 
                    ind -= 1 
                    poly[()] = num 
                buckets.append(poly)
            elif expression[ind] in '+-*':
                symbols.append(expression[ind])
            ind += 1 
        
        # first deal with multi
        # when list would be removed, use reverse range 
        for i in range(len(symbols) - 1, -1, -1):
            if symbols[i] == '*':
                buckets[i] = buckets[i] * buckets.pop(i+1)
                symbols.pop(i)
        
        # deal with + and - 
        if len(buckets) == 0:
            return Poly()
        ans = buckets[0]
        for i in range(len(symbols)):
            if symbols[i] == '+':
                ans = ans + buckets[i+1]
            elif symbols[i] == '-':
                ans = ans - buckets[i+1]
                
        return ans 
