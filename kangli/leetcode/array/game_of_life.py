class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        updates = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbor_count = self.count_neighbors(board, i, j)
                if board[i][j] == 1 :
                    if neighbor_count < 2 or neighbor_count > 3:
                        updates.append([i, j, 0])
                    elif neighbor_count == 2 or neighbor_count == 3:
                        continue
                else:
                    if neighbor_count == 3:
                        updates.append([i, j, 1])
        
        for update in updates:
            i, j, v = update[0], update[1], update[2]
            board[i][j] =v 
            
    
    def count_neighbors(self, board, r, c):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        neighbor_count = 0 
        for d in directions:
            nr, nc = d[0]+r, d[1]+c
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                neighbor_count += board[nr][nc]
        return neighbor_count


'''
Success
Details 
Runtime: 36 ms, faster than 87.88% of Python3 online submissions for Game of Life.
Memory Usage: 13.9 MB, less than 10.00% of Python3 online submissions for Game of Life.
Next challenges: Set Matrix Zeroes
'''
