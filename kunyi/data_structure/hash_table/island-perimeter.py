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
    
    
##### BFS #####
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
                    for delta_x, delta_y in [(-1,0), (1,0), (0, -1), (0, 1)]:
                        new_i, new_j = i + delta_x, j + delta_y
                        if not(0<= new_i < m and 0 <= new_j < n) or grid[new_i][new_j] == 0:
                            ans += 1 
                            
        return ans
