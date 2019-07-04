class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """
    def numberOfBoomerangs(self, points):
        # difficulty: find two points with the same distance
        # for point as the first element of boomerang, like a 
        #   disCount[distance] += 1 (1: [(a,b), (a,c), ..., (a,f)]
        #   ans + P(choose 2 from (b,c,..f))
        ans = 0 
        n = len(points)
        if n <= 2:
            return 0
        for i, point_i in enumerate(points):
            disCount = {}
            for j, point_j in enumerate(points):
                if i == j:
                    continue 
                distance = self.get_distance(point_i, point_j)
                disCount[distance] = disCount.get(distance, 0) + 1 
 
            for dist in disCount:
                if disCount[dist] >= 2:
                    ans += disCount[dist] * (disCount[dist] - 1)
                    
        return ans 
        
    def get_distance(self, point_i, point_j):
        return (point_i[0] - point_j[0]) **2 + (point_i[1] - point_j[1]) **2
