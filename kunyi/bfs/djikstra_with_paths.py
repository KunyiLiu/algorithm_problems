"""
finds the minimum weight path from a start node to every node on the path
the graph is directed with positive weights
"""

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX

# around O(ElogV)


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.prev_path = None
        self.start = None

    def get_neighbours(self, node):
        neighbors = []
        for vertice in range(self.V):
            if self.graph[node][vertice] > 0:
                neighbors.append(vertice)

        return neighbors

    def shortest_path(self, start):
        import heapq, sys
        min_val = sys.maxsize
        queue = []
        prev = [-1] * self.V
        path_weight = [min_val if i != start else 0 for i in range(self.V)]
        heapq.heappush(queue, (0, start))
        while len(queue) > 0:
            current_weight, node = heapq.heappop(queue)
            for neighbor in self.get_neighbours(node):
                if current_weight + self.graph[node][neighbor] < path_weight[neighbor]:
                    path_weight[neighbor] = current_weight + self.graph[node][neighbor]
                    prev[neighbor] = node

                    heapq.heappush(queue, (path_weight[neighbor], neighbor))

        self.prev_path = prev
        self.start = start

    def get_stl(self, end):
        if self.prev_path is None:
            print('Plz update prev path')
            return

        tmp = end
        print_list = []
        while tmp != -1:
            print_list.insert(0, str(tmp))
            tmp = self.prev_path[tmp]

        print('->'.join(print_list))
        return


if __name__ == '__main__':
    # Driver program
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.shortest_path(0)
    g.get_stl(2)
    g.get_stl(5)










