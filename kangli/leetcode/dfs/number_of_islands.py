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
