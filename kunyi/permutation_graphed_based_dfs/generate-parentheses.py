class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # dfs + backtracking 
        # helper - generate combinations with number n parathesis 
        # not-well format 
        self.result = []
        self.dfs(n, {'(': 0, ')': 0}, [])
        return self.result 
        
    def dfs(self, n, count_hash, subset):
        if len(subset) == n * 2:
            # if valid 
            if self.is_valid(subset):
                self.result.append(''.join(subset))
            return 
        
        for para in ['(', ')']:
            if count_hash[para] >= n:
                continue 
            subset.append(para)
            count_hash[para] += 1 
            self.dfs(n, count_hash, subset)
            subset.pop()
            count_hash[para] -= 1 
            
        return 
    
    def is_valid(self, subset):
        stack = []
        for para in subset:
            if para == '(':
                stack.append(para)
            else:
                if len(stack) <= 0:
                    return False 
                stack.pop()
                
        return len(stack) == 0
        
        

#################
class Solution:
    # @param an integer
    # @return a list of string
    # @draw a decision tree when n == 2, and you can understand it!
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res

    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)
