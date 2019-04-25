"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return 
        root = UndirectedGraphNode(node.label)
        queue = [(node, root)]
        visited = {node: root}
    
        while len(queue) > 0:
            node, tmp_root = queue.pop(0)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    tmp_node = UndirectedGraphNode(neighbor.label)
                    tmp_root.neighbors.append(tmp_node)
                    queue.append((neighbor, tmp_node))
                    # if visited, not add to queue, not create new GraphNode
                    visited[neighbor] = tmp_node
                else:
                    tmp_root.neighbors.append(visited[neighbor])
        
        return root
        
 # using dict 
 class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
        
    def cloneGraph(self, node):
        result = self.bfs(node)
        if len(result) == 0:
            return
        dict = {} # old->new
        for n in result:
            dict[n] = UndirectedGraphNode(n.label)
        
        for n in result:
            for ng in n.neighbors:
                dict[n].neighbors.append(dict[ng])
        
        return dict[node]
        
    
    def bfs(self, node):
        import queue
        # record all the node labels
        result = []
        if node is None:
            return result
        q = queue.Queue()
        q.put(node)
        result.append(node)
        while not q.empty():
            node = q.get()
            for n in node.neighbors:
                if n not in result:
                    q.put(n)
                    result.append(n)
        return result
        
        
 # 3. DFS + memo
 # return new node based on the old one
 class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    dict = {} # record node.label: new node
        
    def cloneGraph(self, node):
        if node is None:
            return
        if node.label in self.dict:
            return self.dict[node.label]
        new_node = UndirectedGraphNode(node.label)
        self.dict[node.label] = new_node
        for n in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(n))
        return new_node
