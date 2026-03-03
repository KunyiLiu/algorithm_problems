class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # for the regular LIS issue, dp[i] - the smallest ending element of i length of LIS
        # brute force: for each cell, use dfs
        # topology sorting: create directed edge from smaller val to larger val
        # -> BFS with indegree
        # indegree = 0 -> local minimal, can start LIS
        # Time/Space: O(M*N)

        n, m = len(matrix), len(matrix[0])
        delta_x = [-1, 1, 0, 0]
        delta_y = [0, 0 , -1, 1]
        indegrees = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                for k in range(4):
                    new_i = delta_x[k] + i
                    new_j = delta_y[k] + j
                    if 0 <= new_i < n and 0 <= new_j < m and matrix[new_i][new_j] > matrix[i][j]:
                        indegrees[new_i][new_j] += 1

        q = deque()
        # indegree = 0 -> the smallest elem
        for i in range(n):
            for j in range(m):
                if indegrees[i][j] == 0:
                    q.append((i, j))

        result = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for k in range(4):
                    new_i, new_j = i + delta_x[k], j + delta_y[k]
                    # remove (i, j)
                    if 0 <= new_i < n and 0 <= new_j < m and matrix[new_i][new_j] > matrix[i][j]:
                        indegrees[new_i][new_j] -= 1
                        # now (new_i, new_j) becomes the smaller ones.
                        if indegrees[new_i][new_j] == 0:
                            q.append((new_i, new_j))

            result += 1

        return result




