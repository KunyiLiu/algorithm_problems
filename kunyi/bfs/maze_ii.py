class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # use matrix to record the distance 
        import sys
        if maze is None or len(maze) == 0 or len(maze[0]) == 0:
            return -1 
        m, n = len(maze), len(maze[0])
        distance = [[sys.maxsize] * n for i in range(m)]
        queue = [start]
        # visited
        distance[start[0]][start[1]] = 0 
        
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            x, y = queue.pop(0)
            if x == destination[0] and y == destination[1]:
                return distance[x][y]
            
            for j in range(4):
                new_x, new_y = x + delta_X[j], y + delta_Y[j]
                count = 1 
                while 0<= new_x < m and 0<= new_y < n and maze[new_x][new_y] != 1:
                    # ERROR
                    new_x, new_y = new_x + delta_X[j], new_y + delta_Y[j]
                    count += 1 
                new_x -= delta_X[j]
                new_y -= delta_Y[j]
                count -= 1 
                # never visited
                if distance[new_x][new_y] == sys.maxsize:
                    queue.append([new_x, new_y])
                distance[new_x][new_y] = min(distance[new_x][new_y], count + distance[x][y])
                    
        return -1 
