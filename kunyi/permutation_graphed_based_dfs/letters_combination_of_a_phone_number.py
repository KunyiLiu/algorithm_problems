class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        self.dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if digits is None or len(digits) == 0:
            return []
            
        # all str starting with sub_str from digits, recorded in a set
        self.result = set()
        self.dfs('', digits)
        return list(self.result)
        
    def dfs(self, sub_str, digits):
        if sub_str not in self.result and len(digits) == 0:
            self.result.add(sub_str)
            return 
        
        digit = digits[:1]
        for i in range(len(self.dict[digit])):
            charac = self.dict[digit][i]
            sub_str += charac
            self.dfs(sub_str, digits[1:])
            # string  still nedd to backtrack
            sub_str = sub_str[:-1]
            
        return 
