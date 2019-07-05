class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        ans = 0 
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 4 
                    if i > 0 and grid[i-1][j] == 1:
                        ans -= 2 
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2 
                    
        return ans
