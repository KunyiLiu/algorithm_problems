class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # first find all the index where val == 2 to the queue 
        # level order bfs until queue is empty
        # T(n) = O(n) number of cells
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1 
        m, n = len(grid), len(grid[0])
        queue = []
        visited = [[False] * n for i in range(m)]
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    # ERROR: visited = True for nodes that put on queue before bfs
                    # to prevent it get counted when 4-dimensional move
                    visited[i][j] = True
                if grid[i][j] == 1:
                    fresh_count += 1
                    
        result = 0 
        delta_X = [1,-1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        # ERROR. result -1 not valid if len(queue) = 0 
        if fresh_count == 0:
            return result
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                x, y = queue.pop(0)
                for j in range(4):
                    new_x, new_y = x + delta_X[j], y + delta_Y[j]
                    if 0<= new_x < m and 0<= new_y < n and visited[new_x][new_y] is False and grid[new_x][new_y] == 1:
                        fresh_count -= 1 
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
                        
            result += 1 

        return result - 1 if fresh_count == 0 else -1
