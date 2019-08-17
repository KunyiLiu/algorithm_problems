class TicTacToe:

    def __init__(self, n: int):
        """
        Time: O(n), Space: O(n^2)
        """
        self.board = [[None] * n for i in range(n)]
        self.size = n
     
    def is_win(self, x, y):
        val = self.board[x][y]
        is_row_win = all(item == val for item in self.board[x])
        if is_row_win:
            return True 
        
        is_col_win = all([self.board[i][y] == val for i in range(self.size)])
        if is_col_win:
            return True 
        
        if x == y:
            is_diag_win = all([self.board[i][i] == val for i in range(self.size)])
            if is_diag_win: return True
        if x + y == self.size - 1:
            is_diag_win = all([self.board[i][self.size-1-i] == val for i in range(self.size)])
            if is_diag_win: return True
            
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player 
        # if row == 1 and col == 1:
        #     print(self.board)
        if self.is_win(row, col):
            return player
        return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)




########  O(n) #######
class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row]+=1 if player==1 else -1
        self.col[col]+=1 if player==1 else -1
        if row+col==self.n-1:
            self.diag1+=1 if player==1 else -1
        if row-col==0:
            self.diag2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return 1 if player==1 else 2
        return 0
