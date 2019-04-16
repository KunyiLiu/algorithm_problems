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
