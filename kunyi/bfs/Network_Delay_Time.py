import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm:
        # Always expand the node that currently has the smallest known time
        # Once a node is picked from the min-heap, its shortest time is final
        # BFS + minheap
        # Time complexity: O(E log V^2), Space: O(V + E)
        
        adj_list = {i:[] for i in range(1, n + 1)}
        for u, v, t in times:
            adj_list[u].append((v, t))

        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            total, node = heapq.heappop(minHeap)
            visited.add(node)
            if len(visited) == n:
                return total

            for target, time in adj_list[node]:
                if target not in visited:
                    heapq.heappush(minHeap, (total + time, target))

        return -1


        
