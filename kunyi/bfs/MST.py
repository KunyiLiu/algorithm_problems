# Prim 

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # Euclidian - make sure all the edges are visited once? two city scheduling
        # MST: Starting from city 1, BFS search all next cities, pick up the one with minimal cost, remove this city and add its following cities to BFS searching list.
# Every time one city removed, many added.
        import heapq
        from collections import defaultdict

        visited = [False] * N 
        connection_dict = defaultdict(list)
        for u, v, cost in connections:
            connection_dict[u-1].append((v-1, cost))
            # not necessary 1 -> 2, may be 2 -> 1 
            connection_dict[v-1].append((u-1, cost))
        queue = []   
        heapq.heappush(queue, (0, 0))
        result = 0
        while len(queue) > 0:
            cost, node = heapq.heappop(queue)
            if visited[node]: continue
            visited[node] = True
            result += cost
            for neighbor, diff in connection_dict.get(node, []):
                heapq.heappush(queue, (diff, neighbor))
        
        if all([v is True for v in visited]):
            return result
        return -1
