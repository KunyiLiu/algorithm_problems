class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here
        from collections import defaultdict
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0 
            
        m, n = len(grid), len(grid[0])
        
        dp = defaultdict(lambda: set())
        
        # a list of list then
        # set of sum of the subpath to (i,j)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[(i,j)].add(grid[i][j])
                elif i == 0:
                    dp[(i,j)] = set([(tup + grid[i][j]) for tup in dp[(i,j-1)]])
                elif j == 0:
                    dp[(i,j)] = set([(tup + grid[i][j]) for tup in dp[(i-1,j)]])
                else:
                    tmp_set = dp[(i-1,j)] | dp[(i, j-1)]
                    dp[(i,j)] = set([(tup + grid[i][j]) for tup in tmp_set])
        
            
        return sum(dp[(m-1, n-1)])
    
    
# method 2
class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here
        if grid is None:
            return 0 
            
        return sum(self.helper(0, 0, grid, {}))
    
    # the current sum set to the end from (start, end) 
    def helper(self, row, col, grid, memo):
        m, n = len(grid), len(grid[0])
        if row >= m or col >= n:
            return set()
        
        if row == m -1 and col == n - 1:
            return set([grid[m-1][n-1]])
            
        if (row, col) in memo:
            return memo[(row, col)]
            
        right = self.helper(row + 1, col, grid, memo)
        down = self.helper(row, col + 1, grid, memo)
        memo[(row, col)] =set([(i + grid[row][col]) for i in right.union(down)])
        return  memo[(row, col)]

### recursion + memo #####
class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # recursion + memo 
        # memo[(i,j)] = set([sum of unique paths)
        from collections import defaultdict
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0 
            
        m, n = len(grid), len(grid[0])
        memo = dict()
        result = sum(self.helper(grid, m-1, n-1, memo))
        return result
        
    # the current sum set from (0,0) to (x, y)   
    def helper(self, grid, x, y, memo):
        # exit
        if x < 0 or y < 0:
            return set()
        # initial
        if x == 0 and y == 0:
            memo[(x,y)] = set([grid[0][0]])
            return memo[(x,y)]
            
        if (x, y) in memo:
            return memo[(x, y)]
        
        left = self.helper(grid, x-1, y, memo)
        up = self.helper(grid, x, y-1, memo)
        memo[(x,y)] = set([tup + grid[x][y] for tup in left.union(up)])
        return memo[(x, y)]
        
