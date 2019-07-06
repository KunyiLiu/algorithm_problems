class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def maxAreaOfIsland(self, grid):
        # O(mn(mn))
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        max_result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] is False:
                    tmp_result = self.dfs(grid, visited, i, j, 1)
                    max_result = max(max_result, tmp_result)
                    
        return max_result
        
    def bfs(self, grid, visited, x, y):
        m, n = len(grid), len(grid[0])
        queue = [(x, y)]
        visited[x][y] = True
        tmp_result = 1 
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            old_x, old_y = queue.pop(0)
            for i in range(4):
                new_x, new_y = delta_X[i] + old_x, delta_Y[i] + old_y
                if 0<= new_x < m and 0<= new_y < n and visited[new_x][new_y] is False and grid[new_x][new_y] == 1:
                    tmp_result += 1 
                    visited[new_x][new_y] = True 
                    queue.append((new_x, new_y))
                    
        return tmp_result
        
    def dfs(self, grid, visited, x, y, count):
        # count as initial return 
        visited[x][y] = True 
        m, n = len(grid), len(grid[0])
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        for i in range(4):
            new_x, new_y = delta_X[i] + x, delta_Y[i] + y
            if 0<= new_x < m and 0<= new_y < n and visited[new_x][new_y] is False and grid[new_x][new_y] == 1:
                count = self.dfs(grid, visited, new_x, new_y, count) + 1
                
        return count
