class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        min_distance = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp_distance = self.bfs(grid, i, j)
                    if temp_distance == 0:
                        return -1
                    else:
                        min_distance = max(min_distance, temp_distance)
        return min_distance

    def bfs(self, grid, sr, sc):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q, seen = [(sr, sc)], set()
        seen.add((sr, sc))
        distance = 0
        isolated = True
        while q:
            qsize = len(q)
            for i in range(qsize):
                r, c = q.pop(0)
                if grid[r][c] == 2:
                    return distance
                for d in directions:
                    nr, nc = d[0] + r, d[1] + c
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] != 0:
                        if grid[nr][nc] == 2:
                            isolated = False
                        q.append((nr, nc))
                        seen.add((nr, nc))
            distance += 1
        return distance if not isolated else 0


'''
Submission Result: Accepted 
Next challenges: Walls and Gates
303 / 303 test cases passed.
Status: Accepted
Runtime: 56 ms
Memory Usage: 13.2 MB
Your runtime beats 30.32 % of python3 submission
Your memory usage beats 45.45 % of python3 submissions. 

Related Topics: Breadth-first Search
Similar Questions: Walls and Gates
'''
