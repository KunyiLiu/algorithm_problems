class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    memory_table = {}
    def wordBreak(self, s, wordDict):
        # write your code here
        result = []
        result = self.dfs(s, wordDict)
        return result
        
    def dfs(self, string, wordDict):
        # list I think can be influenced, 
        # because of unchanged address
        if len(string) == 0:
            return 
        if string in self.memory_table:
            return self.memory_table[string] 

        result = []

        for i in range(1, len(string)):
            left = string[:i]
            # until it gets to 'lint'
            print left
            if left not in wordDict:
                continue
            subresult = self.dfs(string[i:], wordDict)
            for sub in subresult:
                result.append(left + ' ' + sub)
        
        # the temp whole string    
        if string in wordDict:
            result.append(string)
            
        self.memory_table[string] = result
        return result
