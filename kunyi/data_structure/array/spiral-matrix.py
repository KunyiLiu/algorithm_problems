##### Time: O(mn) #####
###### similar to bfs, space: O(mn)
class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for i in range(m)]
        x, y = 0, 0
        choice = 0
        visited[0][0] = True
        result.append(matrix[0][0])
        
        while len(result) < m*n:
            direction = directions[choice % 4]
            new_x, new_y = x + direction[0], y + direction[1]
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or visited[new_x][new_y]:
                choice += 1 
            else:
                x, y = new_x, new_y
                result.append(matrix[x][y])
                visited[x][y] = True 
                
        return result 
        
##### O(1) space
    def spiralOrder(self, matrix):
        # Write your code here
        if matrix == []: return []
        up = 0; left = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right: return res
            direct = (direct+1) % 4
