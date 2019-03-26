class Solution(object):
    def exist(self, board, word):
        if len(word) == 0:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False

        for i in range(len(board)):  # Find all matching for first letter
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  # Starting point found
                    if self.helper(board, word, i, j):
                        return True
        return False

    def helper(self, board, word, i, j):  # Recursive process for DFS search

        if len(word) == 1:  # Reach the end, return True
            return True

        board[i][j] = None

        for next_start in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if 0 <= next_start[0] < len(board) and 0 <= next_start[1] < len(board[0]):
                if board[next_start[0]][next_start[1]] == word[1]:
                    if self.helper(board, word[1:], next_start[0], next_start[1]):
                        return True
        return False
