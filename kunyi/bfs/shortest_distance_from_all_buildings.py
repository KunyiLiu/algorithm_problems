class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortestDistance(self, grid):
        # write your code here
        if grid is None or len(grid) == 0:
            return -1 
        m, n = len(grid), len(grid[0])
        
        min_dist = sys.maxint
        dist_grid = [[min_dist] * n for i in range(m)]
        count_grid = [[0] * n for i in range(m)]
        buildings = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(i, j, grid, dist_grid, count_grid, m, n)
                    buildings += 1 
                    
        for i in range(m):
            for j in range(n):
                if count_grid[i][j] == buildings and dist_grid[i][j] < min_dist:
                    min_dist = dist_grid[i][j]
                    
        return -1 if min_dist == sys.maxint else min_dist 
        
    def bfs(self, x, y, grid, dist_grid, count_grid, m, n):
        # count_grid put together with count_grid
        visited_grid = [[False] * n for i in range(m)]
        queue = collections.deque([(x, y, 0)])
        
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        
        while queue:
            old_x, old_y, dis = queue.popleft()
            
            for i in range(4):
                new_x, new_y = old_x + delta_X[i], old_y + delta_Y[i]
                if 0<= new_x < m and 0<= new_y < n and visited_grid[new_x][new_y] is False and grid[new_x][new_y] == 0:
                    visited_grid[new_x][new_y] = True 
                    count_grid[new_x][new_y] += 1 
                    queue.append((new_x, new_y, dis + 1))
                    dist_grid[new_x][new_y] = dis + 1 if dist_grid[new_x][new_y] == sys.maxint else dist_grid[new_x][new_y] + dis + 1 
                    
