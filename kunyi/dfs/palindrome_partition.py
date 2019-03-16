class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if s is None:
            return []
        if len(s) == 0:
            return [[]]
        self.result = []
        self.palin_table = set()
        self.dfs([], s)
        return self.result 
        
    def dfs(self, path, s):
        if s == '':
            self.result.append(path[:])
            return 
        
        for i in range(1, len(s) + 1):
            tmp = s[:i]
            if self.is_palindrome(tmp):
                path.append(tmp)
                self.dfs(path, s[i:])
                path.pop()
                
        return 
    
    def is_palindrome(self, word):
        if len(word) <= 1 or word in self.palin_table:
            self.palin_table.add(word)
            return True 
        
        left, right = 0, len(word) -1 
        while right >= left:
            if word[left] != word[right]:
                return False 
            left += 1  
            right -= 1 
            
        self.palin_table.add(word)
        return True 
