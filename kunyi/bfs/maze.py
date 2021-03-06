class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        import Queue
        if len(maze) == 0 or len(maze[0]) == 0:
            return False 
        queue = Queue.Queue()
        m, n = len(maze), len(maze[0])
        visited = set()  # record starting point 
        queue.put(start)
        while not queue.empty():
            point = queue.get()
            if point == destination:
                return True 
            # update visited, add tmp destination to queue 
            self.bfs(point, visited, maze, queue)
                
        return False 
        
    def bfs(self, point, visited, maze, queue):
        m, n = len(maze), len(maze[0])
        deltaX = [1, -1, 0, 0]
        deltaY = [0, 0, 1, -1]
        x, y = point[0], point[1]
        for i in range(4):
            new_x, new_y = x + deltaX[i], y + deltaY[i]
            final_x, final_y = x, y
            while new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and maze[new_x][new_y] != 1:
                final_x, final_y = new_x, new_y
                new_x, new_y = new_x + deltaX[i], new_y + deltaY[i]
            if (final_x != x or final_y != y) and (final_x, final_y) not in visited:
                queue.put([final_x, final_y])
                visited.add((final_x, final_y))

 #### method 
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        if maze is None or len(maze) == 0:
            return False 
        
        m, n = len(maze), len(maze[0])
        queue = [start]
        visited = [[False] * n for i in range(m)]
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            x, y = queue.pop(0)
            # not level order, can be put here
            # can also modify maze[x][y] = 2
            visited[x][y] = True 
            if x == destination[0] and y == destination[1]:
                return True 
            for i in range(4):
                new_x, new_y = x + delta_X[i], y + delta_Y[i]
                # rolling
                while 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] != 1:
                    new_x += delta_X[i]
                    new_y += delta_Y[i]
                    
                new_x -= delta_X[i]
                new_y -= delta_Y[i]
                if visited[new_x][new_y] is False:
                    queue.append([new_x, new_y])
                    
        return False
