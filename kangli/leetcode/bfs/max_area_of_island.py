class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0 
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    max_area = max(max_area, self.bfs(grid, i, j, seen))
        return max_area 
    
    
    def bfs(self, grid, sr, sc, seen):
        from collections import deque 
        queue = deque([(sr, sc)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen.add((sr, sc))
        m, n = len(grid), len(grid[0])
        area = 1 
        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = d[0]+r, d[1] + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in seen:
                    area += 1 
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return area 
            
'''
726 / 726 test cases passed.
Status: Accepted
Runtime: 92 ms
Memory Usage: 13.5 MB

Related Topics: Array, Depth-first Search
Similar Questions: Number of Islands, Island Perimeter
'''
