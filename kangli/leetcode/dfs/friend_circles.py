class Solution(object):
    def findCircleNum(self, M):
        if not M:
            return 0
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i]:
                continue
            self.dfs(M, i, len(M), visited)
            count +=1
        return count

    def dfs(self, matrix, cur, n, visited):
        if visited[cur]:
            return
        visited[cur] = 1
        for i in range(n):
            if matrix[cur][i] and not visited[i]:
                self.dfs(matrix, i , n, visited)


s = Solution()
print s .findCircleNum([[1, 1, 0, 1], [1, 1, 1, 0], [0, 1, 0, 0], [1, 0, 0, 1]])
