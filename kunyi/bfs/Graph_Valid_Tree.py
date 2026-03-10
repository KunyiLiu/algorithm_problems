######## BFS O(V + E) ###
class Solution:
    from collections import deque
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if there is cycle, separate nodes; bfs - connected graph. 
        # turn edges to adjacency lists 
        # visited - if the nei has visited once, then exists cycle => False
        # if there is a node not visted then separte nodes => false
        # Time/Space complexity: O(V + E)
        if len(edges) < n - 1:
            return False

        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            # record [0, 1], [1, 0] to the adjacency list
            # so when checking if the cycle exists, ensure it does not count it as cycle
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set([0])
        q = deque([(0, -1)])

        while q:
            node, parent = q.popleft()
            for nei in adj_list[node]:
                if parent == nei:
                    continue
                if nei in visited:
                    return False

                visited.add(nei)
                q.append((nei, node))

        return len(visited) == n



### union find Space: O(V), Time: O(V + alpha * E) where alpha stands for amotized ##
class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # cycle detection
        if pu == pv:
            return False

        # attach smaller subtree to the large one
        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1
