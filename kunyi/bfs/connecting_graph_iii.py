class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, num_vertices):
        self.parent = [-1] * num_vertices
        self.count = num_vertices
        
    def find(self, x):
        if self.parent[x] == -1:
            return x 
        if self.parent[x] != -1:
            return self.find(self.parent[x])
        
    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)
        self.parent[x_set] = y_set

    def connect(self, a, b):
        # write your code here
        a_set = self.find(a-1)
        b_set = self.find(b-1)
        if a_set != b_set:
            self.union(a_set, b_set)
            self.count -= 1 

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        # component_set = set([])
        # for i in range(len(self.parent)):
        #     component_set.add(self.find(i))
            
        # return len(component_set)
        
        # 实时维护区域的个数，即若在某一次合并中两个区域合并成一个，那么数量-1
        return self.count
