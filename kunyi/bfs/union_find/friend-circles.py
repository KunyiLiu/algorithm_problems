"""
Time complexity : O(n^3). We traverse over the complete matrix once. Union and find operations take O(n)O(n) time in the worst case.

Space complexity : O(n)O(n). parentparent array of size nn is used.
"""
class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x 
        parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def union(self, parent, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if x_root != y_root:
            parent[y_root] = x_root 
        return 
            
    def findCircleNum(self, M: List[List[int]]) -> int:
        if M is None or len(M) == 0 or len(M[0]) == 0:
            return 0
        
        n = len(M)
        parent = list(range(n))
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    self.union(parent, i, j)
        
        """
        Error:
        1 0 0 1 
        0 1 1 0 
        0 1 1 1 
        1 0 1 1 
        Direct friends: (0, 3), (1, 2), (2, 3)
        
        0 1 2 3 
        0 1 0 0 
        For make the roots table to disjoin set
        """
        for i in range(n):
            self.find(parent, i)
            
        return len(set(parent))
        
######### DFS ############
"""
Time complexity : O(n^2).

Space complexity : O(n)
"""
class Solution:
    def dfs(self, M, visited, ind):
        # make the value of ind, which are connected to ind, to 1 
        n = len(M)
        for j in range(n):
            if visited[j] is False and M[ind][j] == 1:
                visited[j] = True 
                self.dfs(M, visited, j)
        return 

    def findCircleNum(self, M: List[List[int]]) -> int:
        if M is None or len(M) == 0 or len(M[0]) == 0:
            return 0
        
        n = len(M)
        visited = [False] * n 
        count = 0
        for i in range(n):
            if visited[i] is False:
                self.dfs(M, visited, i)
                count += 1 
        
        return count
