class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        n = 3
        count_x, count_o = 0, 0 
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'O':
                    count_o += 1 
                elif board[i][j] == 'X':
                    count_x += 1 
                    
        if not(count_o == count_x or count_x == count_o + 1):
            return False 
        
        is_win_o = self.is_win(board, 'O')
        is_win_x = self.is_win(board, 'X')
        
        if is_win_o and is_win_x: return False
        if is_win_x and count_o == count_x: return False
        if is_win_o and count_x == count_o + 1: return False
        
        return True 
    
    def is_win(self, board, sign):
        n = 3 
        for i in range(n):
            if all([board[i][j] == sign for j in range(n)]):
                return True 
            
        for j in range(n):
            if all([board[i][j] == sign for i in range(n)]):
                return True 
            
        if all([board[i][i] == sign for i in range(n)]):
            return True
        
        if all([board[i][n-1-i] == sign for i in range(n)]):
            return True
        
        return False
