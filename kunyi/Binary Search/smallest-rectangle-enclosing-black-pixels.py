###########  Method 1. BFS #########
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # record the number of cols with 1 
        # and number of rows with 1 
        # BFS O(mn)
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return 0
        m, n = len(image), len(image[0])
        visited = [[False] * n for i in range(m)]
        count_row, count_col = set([]), set([])
        queue = [(x, y)]
        visited[x][y] = True
        # error 1. while not []
        while len(queue) > 0:
            node = queue.pop(0)
            count_row.add(node[0])
            count_col.add(node[1])
            self.bfs(image, visited, node[0], node[1], queue)
        
        return len(count_col) * len(count_row)
        
          
    def bfs(self, image, visited, x, y, queue):
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        m, n = len(image), len(image[0])
        for i in range(4):
            new_x = x + delta_X[i]
            new_y = y + delta_Y[i]
            # error 2. 1 & '1'
            if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] is False and image[new_x][new_y] == '1':
                queue.append((new_x, new_y))
                visited[new_x][new_y] = True 
                
        return
        
########## Method 2. Binary Search ############
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # binary search 
        # find the first col with '1', and last col with '1'
        # similar to row 
        # (last_col - first_col + 1) * (last_row - first_row + 1)
        # Time: T(n) + T(m) = T(n/2) + O(n) + T(m/2) + O(m) = O(m) + O(n)
        
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return 0 
        m, n = len(image), len(image[0])
        # get the first col
        first_col = y 
        start, end = 0, y 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.is_check_col(image, mid):
                end = mid 
            else:
                start = mid 
        first_col = start if self.is_check_col(image, start) else end 
        
        # get the last col 
        start, end = y, n - 1
        last_col = y  
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.is_check_col(image, mid):
                start = mid 
            else:
                end = mid 
                
        last_col = end if self.is_check_col(image, end) else start 
        
        # get the first row 
        first_row = x 
        start, end = 0, x 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.is_check_row(image, mid):
                end = mid 
            else:
                start = mid 
        first_row = start if self.is_check_row(image, start) else end 
        
        last_row = x 
        start, end = x, m - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if self.is_check_row(image, mid):
                start = mid 
            else:
                end = mid 
        last_row = end if self.is_check_row(image, end) else start
        
        return (last_row - first_row + 1) * (last_col - first_col + 1)
        
    def is_check_row(self, image, row):
        for ch in image[row]:
            if ch == '1':
                return True 
        return False 
        
    def is_check_col(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True 
                
        return False
