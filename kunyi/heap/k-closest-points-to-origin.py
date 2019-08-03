class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # small to large
        # KlogN + N 
        import heapq
        if points is None or len(points) == 0:
            return []
        heap = [(self.distance(point[0], point[1]), i) for i, point in enumerate(points)]
        heapq.heapify(heap)
        result = []
        for i in range(K):
            v, ind = heapq.heappop(heap)
            result.append(points[ind])
            
        return result
        
    def distance(self, x, y):
        return (x*x + y*y)**0.5
        
