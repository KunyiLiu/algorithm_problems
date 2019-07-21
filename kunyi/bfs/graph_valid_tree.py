################# union find #################
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        # try using union find
        # acyclic + connected
        self.union_list = [-1 for i in range(n)]
        for u,v in edges:
            u_set = self.find(u)
            v_set = self.find(v)
            if u_set == v_set:
                return False 
            else:
                self.union(u_set, v_set)
 
        return self.union_list.count(-1) == 1 
        
    def find(self, u):
        if self.union_list[u] == -1:
            return u 
        return self.find(self.union_list[u])
        
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.union_list[x_set] = y_set
        
        
############ bfs ###################
# connected + len(edges) == n-1
class Solution:
    """
    @param: n: An integer
    @param: edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """ 
    def validTree(self, n, edges):
        #  connected, acyclic 
        import collections, queue
        if len(edges) != n-1:
            return False
        # set up adjacency list
        neighbours = collections.defaultdict(list)
        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])
        
        # connected 
        #q = []
        #index = 0
        #q.append(0)
        #while index < len(q):
        #    cur = q[index]
        #    nlist = neighbours[cur]
        #    for node in nlist:
        #        if node not in q:
        #            q.append(node)
        #    index += 1
        import queue
        q = queue.Queue()
        q.put(0)
        result = {0}
        while not q.empty():
            node = q.get()
            for i in neighbours[node]:
                if i not in result:
                    q.put(i)
                    result.add(i)
        #return len(q) == n
        return len(result) == n
