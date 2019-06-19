class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    delta_X = [1, -1, 0, 0]
    delta_Y = [0, 0, 1, -1]
    
    def numberofDistinctIslands(self, grid):
        # Difficulty: how to record the shape of islands
        # using set to collect the traces?
        # note:
        # 111    and   11
        # 1            11 same 
        # so we keep track of the relative position
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1 
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for i in range(m)]
        
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] is False:
                    aisland = []
                    self.dfs(i, j, grid, i, j, aisland, visited)
                    islands.add(tuple(aisland))
                    
        return len(islands)
        
    def dfs(self, x, y, grid, start_x, start_y, aisland, visited):
        m, n = len(grid), len(grid[0])
        aisland.append((x - start_x, y - start_y))
        visited[x][y] = True 
        
        for i in range(4):
            new_x, new_y = x + self.delta_X[i], y + self.delta_Y[i]
            if 0<= new_x < m and 0<= new_y < n and grid[new_x][new_y] == 1 and visited[new_x][new_y] is False:
                self.dfs(new_x, new_y, grid, start_x, start_y, aisland, visited)
                
        return 
