class Solution:
    """
    @param edges: List[List[int]]
    @return: List[int]
    """
    def find(self, parent, x):
        if parent[x] == -1:
            return x 
        parent[x] = self.find(parent, parent[x])
        return parent[x]
        
    def union(self, parent, x, y):
        x_parent = self.find(parent, x)
        y_parent = self.find(parent, y)
        if x_parent == y_parent:
            return True 
        parent[x_parent] = y_parent
        return False 
    
    def findRedundantConnection(self, edges):
        # write your code here
        N = 0 
        if edges is None or len(edges) == 0:
            return []
            
        for u, v in edges:
            N = max(N, u, v)
        parent = [-1] * (N+1)
        for u, v in edges:
            if self.union(parent, u, v):
                return [u, v]
                
        return []
