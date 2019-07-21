class Solution:
    def hasPath(self, maze, start, destination):

        Q = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        while Q:
            i, j = Q.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True
            
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])
        
        return False
        

'''
Success
Details 
Runtime: 436 ms, faster than 15.35% of Python3 online submissions for The Maze.
Memory Usage: 13.2 MB, less than 98.44% of Python3 online submissions for The Maze.
Next challenges:
The Maze III
The Maze II

Related Topics: Breadth-first Search, Depth-first Search
'''