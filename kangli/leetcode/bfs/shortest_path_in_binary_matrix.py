class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        from collections import deque 
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        distance = 1 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                r, c = queue.popleft()
                grid[r][c] = 2
                if (r, c) == (m-1, n-1):
                    return distance
                for d in directions:
                    nr, nc = d[0]+r, d[1]+c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
            distance += 1 
        return -1
                        
                        
'''
Success
Details 
Runtime: 660 ms, faster than 74.67% of Python3 online submissions for Shortest Path in Binary Matrix.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Shortest Path in Binary Matrix.
Next challenges: The Maze III, Find Bottom Left Tree Value

Related Topics: Breadth-first Search
'''
