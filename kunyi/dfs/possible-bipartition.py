class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # color the [0] * n as 1 and 2, is graph bipartite?
        if dislikes is None or len(dislikes) == 0:
            return True 
        
        colors = [0] * (N + 1)
        tag = 1 
        dislikes = sorted(dislikes)
        for u, v in dislikes:
            if colors[u] and colors[v]:
                if colors[u] == colors[v]:
                    return False
            elif colors[u]:
                colors[v] = - colors[u]
            elif colors[v]:
                colors[u] = - colors[v]
            else:
                # cannot decide if assign tag or -tag to this one
                colors[u] = tag
                colors[v] = - tag
        print(colors)
        return True
        
######## traverse all nodes and edges, time: O(N + E) #####
##### space O(N + E) space of colors and edges ######

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # color the [0] * n as 1 and 2, is graph bipartite?
        if dislikes is None or len(dislikes) == 0:
            return True 
        
        colors = [0] * (N + 1)
        graph = [[] for i in range(N+1)]
        # convert dislikes to adjacency list 
        for u, v in dislikes:
            graph[u].append(v) 
            graph[v].append(u)
        for i in range(1, N+1):
            if colors[i] == 0 and not self.dfs(i, colors, graph, 1):
                return False
            
        return True
    
    def dfs(self, start, colors, graph, tag):
        colors[start] = tag
        for ind in graph[start]:
            if colors[ind] == 0 and not self.dfs(ind, colors, graph, -tag):
                return False 
            if colors[ind] != -tag:
                return False 
            
        return True
