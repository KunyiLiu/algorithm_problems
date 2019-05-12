############   faster, collections.deque ########
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxint for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxint
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
  
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)])
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1 
                        
############# level order ################
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # reverse - building to post office
        # dist_grid, visited_grid, building_count_grid
        # O(n^2 * n^2)
        if grid is None or len(grid) == 0:
            return -1 
        import sys
        min_dist = sys.maxsize
        m, n = len(grid), len(grid[0])
        dist_grid = [[min_dist]*n for i in range(m)]
        building_count_grid = [[0]*n for i in range(m)]
        
        count_building = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(i, j, grid, dist_grid, building_count_grid)
                    count_building += 1 
        
        for i in range(m):
            for j in range(n):
                if building_count_grid[i][j] == count_building and dist_grid[i][j] < min_dist:
                    min_dist = dist_grid[i][j]
                    
        return - 1 if min_dist == sys.maxsize else min_dist
        
    def bfs(self, x, y, grid, dist_grid, building_count_grid):
        import Queue, sys
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        queue = Queue.Queue()
        m, n = len(grid), len(grid[0])
        visited_grid = [[False]*n for i in range(m)]
        
        queue.put((x, y))
        level = 1
        
        while not queue.empty():
            qsize = queue.qsize()
            for i in range(qsize):
                old_x, old_y = queue.get()
                
                for j in range(4):
                    new_x = old_x + delta_X[j]
                    new_y = old_y + delta_Y[j]
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 0 and visited_grid[new_x][new_y] is False:
                        queue.put((new_x, new_y))
                        visited_grid[new_x][new_y] = True
                        building_count_grid[new_x][new_y] += 1 
                        dist_grid[new_x][new_y] = level if dist_grid[new_x][new_y] == sys.maxsize else dist_grid[new_x][new_y] + level 
                        
            level += 1
