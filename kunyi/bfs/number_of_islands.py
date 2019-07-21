# dfs
class Solution:
    """
    @param: grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid == []:
            return 0
        m,n = len(grid), len(grid[0])
        visited = [[False for i in range(n)] for i in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == False:
                    self.dfs(i, j, grid, visited, m, n)
                    count += 1
        return count
        
    def dfs(self, i, j, grid, visited, m, n):
        # preorder
        visited[i][j] = True
        deltaX = [1,0,-1,0]
        deltaY = [0,1,0,-1]
        for k in range(4):
            newx = i + deltaX[k]
            newy = j + deltaY[k]
            if 0 <= newx < m and  0 <= newy < n and visited[newx][newy] == False and grid[newx][newy] == 1:
                    self.dfs(newx, newy, grid, visited, m, n)
        return
        
# bfs 
  class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # O(rc)
        # first scan through grid to get the land list 
        # then use bfs to update the visited matrix, 
        # if node has been visited, do not increment the result 
        result = 0 
        if len(grid) == 0 or len(grid[0]) == 0:
            return result 
            
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.bfs(i, j, visited, grid)
                    result += 1
            
        return result 
        
    def bfs(self, i, j, visited, grid):
        import Queue
        m, n = len(grid), len(grid[0])
        queue = Queue.Queue()
        queue.put((i, j))
        deltaX = [-1, 1, 0, 0]
        deltaY = [0, 0, -1, 1]
        while not queue.empty():
            node = queue.get()
            x, y = node[0], node[1]
            visited[x][y] = True 
            for i in range(4):
                new_x, new_y = x + deltaX[i], y + deltaY[i]
                if 0<= new_x < m and 0<= new_y < n and visited[new_x][new_y] is False and grid[new_x][new_y]== 1:
                    queue.put((new_x, new_y))
