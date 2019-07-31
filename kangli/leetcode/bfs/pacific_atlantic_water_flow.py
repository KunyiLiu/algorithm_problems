class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        from collections import deque
        pacific, atlantic = set(), set()
        queue = deque([])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    queue.append((i, j))
                if i == 0:
                    queue.append((i, j))
        self.bfs(queue, matrix, pacific)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == len(matrix[0])-1:
                    queue.append((i, j))
                if i == len(matrix)-1:
                    queue.append((i, j))
        self.bfs(queue, matrix, atlantic)
        res = list(pacific.intersection(atlantic))
        for p in res:
            p = [p[0], p[1]]
        return res 
        
    def bfs(self, queue, matrix, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(matrix), len(matrix[0])
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))
            for d in directions:
                nr, nc = d[0]+r, d[1]+c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and matrix[r][c] <= matrix[nr][nc]:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    

'''
Success
Details 
Runtime: 356 ms, faster than 22.69% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.3 MB, less than 8.96% of Python3 online submissions for Pacific Atlantic Water Flow.
Next challenges: Minimum Depth of Binary Tree, Perfect Squares, Shortest Path in Binary Matrix
'''
