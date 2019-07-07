class Solution:
    def updateMatrix(self, matrix):
        result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1 and (i, j):
                    distance_to_zero = self.bfs(matrix, i, j)
                    result[i][j] = distance_to_zero
        return result

    def bfs(self, matrix, sr, sc):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = [(sr, sc)]
        m, n = len(matrix), len(matrix[0])
        seen = set()
        seen.add((sr, sc))
        distance = 0
        while q:
            qsize = len(q)
            for i in range(qsize):
                r, c = q.pop(0)
                if matrix[r][c] == 0:
                    return distance
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen:
                        q.append((nr, nc))
                        seen.add((nr, nc))
            distance += 1
        return distance

'''
Submission Result: Accepted 
Next challenges: Number of Distinct Islands II, N-ary Tree Level Order Traversal, Robot Room Cleaner
48 / 48 test cases passed.
Status: Accepted
Runtime: 832 ms
Memory Usage: 15.8 MB

Related Topics: Depth-first Search, Breadth-first Search
'''
