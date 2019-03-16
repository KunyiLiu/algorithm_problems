class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if A is None:
            return []
        if len(A) == 0:
            return [[]]
        self.result = []
        self.A = sorted(A)
        self.k = k
        self.dfs([], 0, target)
        return self.result 
        
    def dfs(self, subset, ind, target):
        if target < 0 or len(subset) > self.k:
            return 
        if len(subset) == self.k and target == 0:
            self.result.append(subset[:])
            return 
        for i in range(ind, len(self.A)):
            subset.append(self.A[i])
            self.dfs(subset, i+1, target - self.A[i])
                
            subset.pop()
        
        return 
        
        
 # method 2
 class Solution:

    def kSumII(self, A, k, target):
        anslist = []
        self.dfs(A, k, target, 0, [], anslist)
        return anslist

    def dfs(self, A, k, target, index, onelist, anslist):
        if target == 0 and k == 0:
            anslist.append(onelist)
            return
            
        if len(A) == index or target < 0 or k < 0:
            return
        
        # do not choose the element   
        self.dfs(A, k, target, index + 1, onelist, anslist)
        # choose the element
        self.dfs(A, k - 1, target - A[index],  index + 1 , onelist + [A[index]], anslist)
