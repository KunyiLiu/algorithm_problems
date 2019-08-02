from collections import defaultdict


class Graph:
    """
    Using adjacency list to represent undirected graph
    """

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # u, v is node
        self.graph[u].append(v)


class Solution:
    def __init__(self, graph_instance):
        self.graph = graph_instance.graph
        self.num_vertices = graph_instance.num_vertices

    def find(self, parent, i):
        # i is the index of parent list, represents the node number
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

    def is_cyclic(self):
        parent = [-1] * self.num_vertices

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x_set = self.find(parent, i)
                y_set = self.find(parent, j)
                if x_set == y_set:
                    return True
                self.union(parent, x_set, y_set)

        return False


if __name__ == '__main__':
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    solution = Solution(g)

    print 'Graph contains cycles? {}'.format(solution.is_cyclic())
