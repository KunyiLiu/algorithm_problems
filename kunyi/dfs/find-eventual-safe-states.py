#### space/time: O(V+E) traveres all nodes and edges #######

class Solution:
    """
    @param graph: a 2D integers array
    @return: return a list of integers
    """
    def eventualSafeNodes(self, graph):
        # write your code here
        if graph is None or len(graph) == 0:
            return []
            
        # 0 for unvisited; 1 for visiting; 2 for visited
        # every loop, 即将从一个节点退出时, 如果它没有被标记为不安全的, 那么将它标记为已访问过.
        n = len(graph)
        self.ans = set()
        for i in range(n):
            self.dfs(i, graph, set([i]))
        return sorted(self.ans)
        
    def dfs(self, start, graph, visited):
        for ind in graph[start]:
            if ind in visited:
                return False
            if ind in self.ans:
                continue
          
            visited.add(ind)
            if not self.dfs(ind, graph, visited):
                return False
            visited.remove(ind)
            
        self.ans.add(start)        
        return True
