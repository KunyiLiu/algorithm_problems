class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # reverse idea - from gate to INF 
        # first record the indices of gates, put them into queue 
        # pop them based on level order
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return rooms 
        m, n = len(rooms), len(rooms[0])
        distance = 1
        INF = 2**31 - 1
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
        
        delta_X = [1,-1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                x, y = queue.pop(0)
                for j in range(4):
                    new_x, new_y = x + delta_X[j], y + delta_Y[j]
                    if 0<= new_x < m and 0<= new_y < n and rooms[new_x][new_y] == INF:
                        # new_x, new_y won't get revisited
                        rooms[new_x][new_y] = distance
                        queue.append((new_x, new_y))
                        
            distance += 1 
        
        return rooms
