class Solution(Object):
    def hasPath(self, maze, start, destination):
        r, c = len(maze), len(maze[0])

        def dfs(x, y, visited):
            if (x, y) in visited:
                return False
            visited.add((x, y))
            if x == destination[0] and y == destination[1]:
                return True

            for i, j in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                newX, newY = x, y
                while 0 <= newX + i < r and 0 <= newY +j < c and maze[newX+i][newY+j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY, visited):
                    return True
            return False

        return dfs(start[0], start[1], set())




#
# class Solution(object):
#     def hasPath(self, maze, start, destination):
#         visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
#         print self.dfs(maze, visited, start, destination)
#
#     def dfs(self, maze, visited,  start, destination):
#         x, y = start[0], start[1]
#         visited[x][y] = True
#         if x == destination[0] and y == destination[1]:
#             return True
#         if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or visited[x][y]:
#             return False
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         for i in range(4):
#
#             while x >= 0 and x < len(maze) and y >=0 and y <len(maze[0]) and maze[x][y] != 1:
#                 x += directions[i][0]
#                 y += directions[i][1]
#             x -= directions[i][0]
#             y -= directions[i][1]
#
#             if self.dfs(maze, visited, [x, y], destination):
#                 return True
#         return False
#
#
# s = Solution()
# s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0, 4], [4, 4])
