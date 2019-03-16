class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates is None:
            return []
        if len(candidates) == 0:
            return [[]]
            
        self.candidates = sorted(candidates)
        self.result = []
        self.dfs([], 0, target)
        return self.result 
        
    def dfs(self, subset, ind, target):
        if target < 0:
            return 
        if target == 0:
            self.result.append(subset[:])
            return 
        
        for i in range(ind, len(self.candidates)):
            # depuplicate 
            if i > ind and self.candidates[i-1] == self.candidates[i]:
                continue 
            subset.append(self.candidates[i])
            self.dfs(subset, i, target - self.candidates[i])
            subset.pop()
            
        return
