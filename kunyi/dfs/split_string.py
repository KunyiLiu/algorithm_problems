class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if s is None:
            return []
        if len(s) == 0:
            return [[]]
        self.result = []
        self.s = s
        self.dfs([], 0)
        return self.result 
        
    def dfs(self, subset, ind):
        if ind == len(self.s):
            self.result.append(subset[:])
            return 
        
        subset.append(self.s[ind])
        self.dfs(subset, ind + 1)
        subset.pop()

        if ind + 1 < len(self.s):
            subset.append(self.s[ind:(ind+2)])
            self.dfs(subset, ind + 2)
            subset.pop()
        
        return
        
 # method 2       
 def splitString(self, s):
        # write your code here
        result = []
        self.dfs(result, [], s)
        return result 
    
    def dfs(self, result, path, s):
        if s == "":
            result.append(path[:]) #important: use path[:] to clone it
            return 
        for i in range(2):
            if i+1 <= len(s):
                path.append(s[:i+1])
                self.dfs(result, path, s[i+1:])
                path.pop()
