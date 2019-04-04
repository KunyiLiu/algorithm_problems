# method 1. DO
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # DP O(n) try bottom up 
        import sys
        n = len(triangle)
        # dp[i][j] - the min sum from (i,j) to bottom
        dp = [[sys.maxsize for i in range(n)] for j in range(n)]
        
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i]
            
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
                
        return dp[0][0]
        
        

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    # method 2: traverse (best global value)
    # def minimumTotal(self, triangle):
    #     # method 1: traverse O(2^n), n - level
    #     import sys
    #     self.best = sys.maxsize
    #     self.triangle = triangle
    #     self.helper(0, 0, 0)
    #     return self.best 
    
    # # get the sum from (0,0) to (x,y) (x,y not included)   
    # def helper(self, x, y, _sum):
    #     if x == len(self.triangle):
    #         if _sum < self.best:
    #             self.best = _sum 
                
    #         return 
        
    #     if y < len(self.triangle):
    #         self.helper(x + 1, y, _sum + self.triangle[x][y])
    #         self.helper(x + 1, y + 1, _sum + self.triangle[x][y])
            
    #     return 
    
    # DQ + memorization (best in returned value)
    def minimumTotal(self, triangle):
        # DQ + Memorization O(n^2), each node only visited once
        self.hash_table = {}
        self.triangle = triangle
        result = self.helper(0, 0)
        return result
        
    def helper(self, x, y):
         # minimum sum from (x, y) to bottom
        import sys
        if x == len(self.triangle):
            return 0 
            
        if (x,y) in self.hash_table:
            return self.hash_table[(x,y)]
        
        if y < len(self.triangle):
            self.hash_table[(x,y)] = self.triangle[x][y] + min(self.helper(x+1, y), self.helper(x+1, y+1))  
            
        return self.hash_table[(x,y)]
