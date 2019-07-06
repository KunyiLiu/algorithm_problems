class Solution:
    def islandPerimeter(self, grid):
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    perimeter += self.count_water_edges(grid, i, j)
        return perimeter

    def count_water_edges(self, grid, i, j):
        edges = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in directions:
            if i + d[0] < 0 or j + d[1] < 0 or i + d[0] >= m or j + d[1] >= n:
                edges += 1
                continue
            if grid[i + d[0]][j] == 0 or grid[i][j + d[1]] == 0:
                edges += 1
        return edges


'''
Submission Result: Accepted 
Next challenges: Max Area of Island, Flood Fill, Coloring A Border
5833 / 5833 test cases passed.
Status: Accepted
Runtime: 368 ms
Memory Usage: 13.5 MB

Related Topics: Hash Table
Similar Questions: Max Area of Island, Flood Fill, Coloring A Border
'''
