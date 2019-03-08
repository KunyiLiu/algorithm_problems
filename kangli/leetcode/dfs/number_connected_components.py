
'''
Given n nodes numbered 0 to n-1 and a list of edges in an undirected graph, count the number of connected components.
There are no duplicate edges.
Companies Amazon(3), LInkedin(2)
Similar question: number of islands, graph valid tree, friend circles
'''
class Solution(object):
    def countComponents(self, n, edges):
        adj_list = {}
        for i in range(n):
            if i not in adj_list:
                adj_list[i] = []
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                self.dfs(visited, i, adj_list)
        return count

    def dfs(self, visited, index, adj_list):
        visited.add(index)
        for node in adj_list[index]:
            if node not in visited:
                self.dfs(visited, node, adj_list)


s = Solution()
s.countComponents(5, [[0,1],[1,2],[3,4]])

# visit = {}
# for i in range(5):
#     visit[i] = []
#     visit[i].append(2*i)
# print visit
#
# for i in range(5):
#     visit[i].append("bl")
# print visit
