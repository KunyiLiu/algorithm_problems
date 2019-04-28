"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        # record indegree of each node 
        # find the node with indegree = 0, and put it to queue
        # get the node from queue and remove all the connected edges
        # put the node with indegree = 0 to queue 
        result = []
        if graph is None:
            return result 
            
        indegrees = {}
        for node in graph:
            indegrees[node] = 0
            
        for node in indegrees:
            for in_node in node.neighbors:
                indegrees[in_node] += 1 
        
        # find the node with 0 indegree
        import Queue 
        queue = Queue.Queue()
        for node, degree in indegrees.items():
            if degree == 0:
                queue.put(node) 
            
        while not queue.empty():
            node = queue.get()
            result.append(node)
            for in_node in node.neighbors:
                indegrees[in_node] -= 1 
                if indegrees[in_node] == 0:
                    queue.put(in_node)
                    
        return result 
        
 """
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # adjacency list
        ind = {}
        result = []
        if graph == []:
            return result
        # initiate ind (indegree dict)
        for node in graph:
            if node not in ind:
                ind[node] = 0
            for n in node.neighbors:
                if n not in ind:
                    ind[n] = 1
                else:
                    ind[n] += 1
        
        result = []
        for node in graph:
            if ind[node] == 0:
                self.dfs(node, ind, result)
        return result
            
    def dfs(self, node, ind, result):
        ind[node] = -1
        result.append(node)
        for i in node.neighbors:
            ind[i] -= 1
            if ind[i] == 0:
                self.dfs(i, ind, result)
