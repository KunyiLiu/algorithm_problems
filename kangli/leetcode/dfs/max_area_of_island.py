class Solution(object):
    def maxAreaOfIsland(self, grid):
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = self.dfs(grid, i, j)
                    maxArea = max(maxArea, size)
        return maxArea

    def dfs(self, grid, r, c):
        area = 1
        grid[r][c] = 2
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row = r + dx
            col = c + dy
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                area += self.dfs(grid, row, col)
        return area
