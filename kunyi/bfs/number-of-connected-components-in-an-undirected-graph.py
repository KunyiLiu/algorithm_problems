####### union find ###########
class Solution:
    def find(self, parent, u):
        if parent[u] == -1:
            return u 
        return self.find(parent, parent[u])
    
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [-1] * n 
        for u, v in edges:
            u_set = self.find(parent, u)
            v_set = self.find(parent, v)
            if u_set != v_set:
                parent[u_set] = v_set
                    
        count = set()
        for i in range(n):
            i_subset = self.find(parent, i)
            count.add(i_subset)
            
        return len(count)
        
####### union find with path compression ##########
class Solution:
    def find(self, parent, u):
        # make the found root as parent of x so that
        # we dont need to traverse the intermediate nodes
        if parent[u] != u:
            parent[u] = self.find(parent, parent[u])
        return parent[u]
    
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [_ for _ in range(n)]
        for v, w in edges:
            parent[self.find(parent, v)] = self.find(parent, w)
        return len(set(map(lambda x: self.find(parent, x), parent)))
