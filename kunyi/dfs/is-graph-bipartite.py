################# DFS ###############
class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # dfs 
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] == 0 and not self.dfs(graph, i, colors, 1):
                return False 
                
        return True 
        
    def dfs(self, graph, node, colors, c):
        # if we can color the node and its ajacent nodes successfully
        colors[node] = c 
        for nxt in graph[node]:
            if colors[nxt] == 0 and not self.dfs(graph, nxt, colors, -c):
                return False 
            if colors[nxt] != -c:
                return False
                
        return True 
        
############## BFS ##############
class Solution:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # 我们会从一点出发，利用bfs 对该点以及其邻居点上色且相邻点不能有同色，如果有同色，就不能是bipartite
        n = len(graph)
        colors = [0 for i in range(n)]
        
        for i in range(n):
            if colors[i] != 0:
                continue 
            
            # start from one source
            colors[i] = 1 
            queue = [i]
            while len(queue) > 0:
                node = queue.pop(0)
                for neightbor in graph[node]:
                    if colors[neightbor] == 0:
                        colors[neightbor] = -colors[node] 
                        queue.append(neightbor)
                    elif colors[neightbor] != -colors[node]:
                        return False 
                        
        return True 
