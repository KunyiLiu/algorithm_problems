class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValid(self, nums):
        # nums iterator
        num_hash = {}
        for num in nums:
            if num in num_hash and num != '.':
                return False
            else:
                num_hash[num] = 1 
        return True 

    def isValidSudoku(self, board):
        # write your code here
        for row in board:
            is_row_valid = self.isValid(row)
            if not is_row_valid:
                return False
        for col_ind in range(len(board[0])):
            col = [i[col_ind] for i in board]
            is_col_valid = self.isValid(col)
            if not is_col_valid:
                return False
        # square [0, 0], [3, 0], [6, 0], [0, 3], []
        for i in range(0, 9, 3):
            for j in range(0, 9,3):
                # (i, j) (i + 2, j + 2)
                tmp = board[i][j:(j+3)] + board[i+1][j:(j+3)] + board[i+2][j:(j+3)]
                is_square_valid = self.isValid(tmp)
                if not is_square_valid:
                    return False
                    
        return True
