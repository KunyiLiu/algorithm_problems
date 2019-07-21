#######  visited put right after x,y = queue.pop(0) ######
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if board == None or len(board) == 0 or len(board[0]) == 0:
            return 
        m, n = len(board), len(board[0])
        for i in range(m):
            self.bfs(board, i, 0, m, n)
            self.bfs(board, i, n - 1, m, n)
        for j in range(n):
            self.bfs(board, 0, j,m ,n)
            self.bfs(board, m - 1, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
        return board
        
        
        
    def bfs(self, board, x, y, m, n):
        if board[x][y] == 'X':
            return 
        import queue
        deltaX = [1,0,-1,0]
        deltaY = [0,1,0,-1]
        q = queue.Queue()
        q.put((x, y))
        board[x][y] = 1
        while not q.empty():
            node = q.get()
            for k in range(4):
                newX = node[0] + deltaX[k]
                newY = node[1] + deltaY[k]
                if 0<= newX < m and 0<= newY < n and board[newX][newY] == 'O':
                    board[newX][newY] = 1
                    q.put((newX, newY))
                    
############ visited put in 4-dimensional move ##########
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # multiple sources connecting problem
        # record the sources 'O' where x=0 or m-1, y=0 or n-1
        # mark the connected one to '1'
        if board is None or len(board) == 0:
            return 
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
                
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m-1][j] == 'O':
                queue.append((m-1, j))
        
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            x, y = queue.pop(0)
            board[x][y] = '1'
            for i in range(4):
                new_x, new_y = x + delta_X[i], y + delta_Y[i]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    queue.append((new_x, new_y))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '1':
                    board[i][j] = 'O'
                    
        return board
