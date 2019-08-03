"""
make a union find parent array
push new roads to min heap
every time, choose the one with smallest distance, and invoke union, if x_root != y_root, select this one, and remove
from set union until count(set) == 1
"""
# Time Complexity: O(numNewroad) + O(numRoad*numCities) + O(numCities*lognumNewroad)
# Space: O(numNewroad)


class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if x_root == y_root:
            return False

        # union the root of set
        parent[y_root] = x_root
        return True

    def mst(self, numCities, numRoad, roadsAvailable, numNewroad, Cost):
        import heapq
        heap = [(count, [u, v]) for u, v, count in Cost]
        heapq.heapify(heap)

        parent = list(range(numCities + 1))
        for u, v in roadsAvailable:
            self.union(parent, u, v)

        for x in range(1, numCities + 1):
            self.find(parent, x)
        count_set = len(set(parent))

        result = 0
        while count_set != 1:
            if len(heap) == 0:
                break
            count, edge = heapq.heappop(heap)
            if self.union(parent, edge[0], edge[1]):
                count_set -= 1
                result += count

        return result


if __name__ == '__main__':
    numCities = 6
    numRoad = 3
    roadsAvailable = [[1, 4], [4, 5], [2, 3]]
    numNewroad = 4
    Cost = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    sol = Solution()
    print(sol.mst(numCities, numRoad, roadsAvailable, numNewroad, Cost))
