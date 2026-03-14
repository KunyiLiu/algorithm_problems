####### Shortest path ######
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dijstrak algorithm: the shortest path from source to dst
        # we need adjancey list for the source: (target, dist)
        # instead of using heap, since it has k step limit, we use level ordering
        # for each level, we pop out all the existing nodes in queue, to check its neighbor and 
        # compare the total dist
        # Time complexity: O(#flights * k), Space: O(#cities + #flights)
        if src == dst:
            return 0

        from collections import defaultdict
        adj_list = defaultdict(list)

        for flight in flights:
            adj_list[flight[0]].append((flight[1], flight[2]))

        # source, total
        q = deque([(src, 0)])
        count = 0
        result = float("inf")

        while q:
            if count > k:
                break

            for i in range(len(q)):
                target, total_cost = q.popleft()
                for nei, cost in adj_list[target]:
                    if nei == dst:
                        result = min(result, total_cost + cost)
                    else:
                        q.append((nei, total_cost + cost))

            count += 1

        # if traverse the whole graph but still not find the result
        return result if result < float("inf") else -1

####### Bellman–Ford Solution #####

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        # distance[i] = cheapest price to reach city i
        dist = [float("inf")] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist[:]   # important: copy previous state

            for u, v, price in flights:
                if dist[u] == float("inf"):
                    continue

                temp[v] = min(temp[v], dist[u] + price)

            dist = temp

        return -1 if dist[dst] == float("inf") else dist[dst]




        
