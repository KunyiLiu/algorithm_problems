class Solution:
    def isValidSudoku(self, board):
        digits = [str(i) for i in range(1, 10)]
        for row in board:
            d = {}
            for j in range(len(row)):
                if row[j] == '.':
                    continue
                elif row[j] not in digits:
                    return False
                elif row[j] in d:
                    return False
                else:
                    d[row[j]] = 1

        for i in range(len(board[0])):
            d = {}
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                elif board[j][i] not in digits:
                    return False
                elif board[j][i] in d:
                    return False
                else:
                    d[board[j][i]] = 1

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                d = {}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == '.':
                            continue
                        if board[k][l] in d:
                            return False
                        else:
                            d[board[k][l]] = 1
        return True

'''
Success
Details 
Runtime: 48 ms, faster than 93.30% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.3 MB, less than 31.16% of Python3 online submissions for Valid Sudoku.
Next challenges:
Sudoku Solver

Related Topics: Hash Table
Similar Questions: Sudoku Solver
'''
