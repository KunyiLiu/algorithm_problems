from collections import defaultdict


class Subset:
    def __init__(self, u, rank):
        self.parent = u
        self.rank = rank


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find set of an element
    # node(uses path compression technique)
    # make the found root as parent of x so that
    # we dont need to traverse the intermediate nodes
    def find(self, subsets, node):
        if subsets[node].parent == node:
            return node
        subsets[node].parent = self.find(subsets, subsets[node].parent)
        return subsets[node].parent

    # A function that does union of two sets
    # of u and v(uses union by rank)
    def union(self, subsets, u, v):
        # Attach smaller rank tree under root
        # of high rank tree(Union by Rank)
        if subsets[u].rank > subsets[v].rank:
            subsets[v].parent = u
        elif subsets[u].rank < subsets[v].rank:
            subsets[u].parent = v
        else:
            subsets[v].parent = u
            subsets[u].rank += 1

    def is_cyclic(self):
        subsets = [Subset(u, 0) for u in range(self.num_vertices)]

        # Iterate through all edges of graph,
        # find sets of both vertices of every
        # edge, if sets are same, then there
        # is cycle in graph.
        for i in self.graph:
            i_subset = self.find(subsets, i)
            for j in self.graph[i]:
                j_subset = self.find(subsets, j)
                if i_subset == j_subset:
                    return True

                # i_subset, j_subset already the parents
                self.union(subsets, i_subset, j_subset)


if __name__ == '__main__':
    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)

    print 'Graph contains cycles? {}'.format(g.is_cyclic())
