class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            self.dfs(board, x, y)
            
        return board
    
    def dfs(self, board, x, y):
        # visited replaced by board == 'E'
        # queue replaced by stack
        m, n = len(board), len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'E':
            return
        if board[x][y] == 'M':
            return
        
        delta_X = [1, -1, 0, 0, 1, -1, 1, -1]
        delta_Y = [0, 0, 1, -1, 1, -1, -1, 1]
        m_count = 0
        for i in range(8):
            new_x, new_y = x + delta_X[i], y + delta_Y[i]
            if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'M':
                m_count += 1 
        # once its ajancent node hits 'M', stop
        # or (0, 2) would be 'B'
        if m_count > 0:
            board[x][y] = str(m_count)
            return 
        board[x][y] = 'B'
        
        for i in range(8):
            new_x, new_y = x + delta_X[i], y + delta_Y[i]
            self.dfs(board, new_x, new_y)
