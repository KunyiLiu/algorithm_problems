'''
Given a 2d grid map of 1's and 0's, count the number of groups of 1's (islands).
Similar questions: Walls and Gates, Number of Islands II, Number of Connected Components in an Undirected Graph,
Number of Distinct Islands, and Max Area of Island
'''
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '#'
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.dfs(grid, i+dx, j+dy)
        else:
            return

s = Solution()
print s.numIslands([['1', '1', 0], [0, 0, 0], [0, 0, 0]])

'''
Success
Details 
Runtime: 80 ms, faster than 69.09% of Python3 online submissions for Number of Islands.
Memory Usage: 13.9 MB, less than 68.10% of Python3 online submissions for Number of Islands.
Next challenges:
Number of Islands II
Number of Connected Components in an Undirected Graph
Number of Distinct Islands
'''


class Solution:
    def numIslands(self, grid):
        seen = set()
        island_count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == '1':
                    island_count += self.bfs(grid, i, j, seen)
        return island_count
    
    def bfs(self, grid, i, j, seen):
        from collections import deque
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        queue = deque([(i, j)])
        seen.add((i, j))
        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = d[0]+r, d[1]+c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and (nr, nc) not in seen:
                    queue.append((nr, nc))
                    seen.add((nr, nc))
        return 1 
          

'''
Success
Details 
Runtime: 80 ms, faster than 70.04% of Python3 online submissions for Number of Islands.
Memory Usage: 17.7 MB, less than 9.53% of Python3 online submissions for Number of Islands.
Next challenges: Surrounded Regions, Walls and Gates, Number of Islands II, 
Number of Connected Components in an Undirected Graph, Number of Distinct Islands

Related Topics: Depth-first Search, Breadth-first Search, Union Find
Similar Questions: Surrounded Regions, Walls and Gates, Number of Islands II, 
Number of Connected Components in an Undirected Graph, Number of Distinct Islands, 
Max Area of Island
'''
