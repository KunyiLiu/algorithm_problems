#### time: O(V+E) traveres all nodes and edges #######
### classic "white-gray-black" DFS algorithm
#### exit our search quickly when we find a cycle - say the result of visiting a node is true if it is eventually safe, otherwise false

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

########
class Solution:
    """
    @param graph: a 2D integers array
    @return: return a list of integers
    """
    def eventualSafeNodes(self, graph):
        # record the nodes that dont walk in cycles
        # white - not started node, grey - started but not confirmed to be valid
        # black - valid nodes 
        """
            the only possibilities are that we've marked the entire subtree black (which must be eventually safe), or it has a cycle and we have only marked the members of that cycle gray.
        """
        if graph is None or len(graph) == 0:
            return []
        n = len(graph)
        colors = [0] * n 
        for i in range(n):
            if colors[i] == 0:
                self.dfs(i, colors, graph)
            
        return [ind for ind, color in enumerate(colors) if color == 2]
        
    def dfs(self, start, colors, graph):
        # if remain gray/1 after dfs, means if it is not valid
        colors[start] = 1 
        for ind in graph[start]:
            if colors[ind] == 0 and not self.dfs(ind, colors, graph):
                return False 
            elif colors[ind] != 2:
                return False
                
        colors[start] = 2 
        return True
