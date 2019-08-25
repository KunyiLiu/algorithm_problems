'''
Success
Details 
Runtime: 472 ms, faster than 17.65% of Python3 online submissions for Word Search.
Memory Usage: 15.3 MB, less than 17.02% of Python3 online submissions for Word Search.
Next challenges: Word Search II
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, (i, j), word):
                        return True
        return False
                    
    def dfs(self, board, start, word):
        m, n = len(board), len(board[0])
        if len(word) < 1:
            return True
        r, c = start[0], start[1]
        if 0 <= r < m and 0 <= c < n and board[r][c] == word[0]:
            board[r][c] = None
            is_down = self.dfs(board, (r+1, c), word[1:])
            is_right = self.dfs(board, (r, c+1), word[1:])
            is_left = self.dfs(board, (r, c-1), word[1:]) 
            is_up = self.dfs(board, (r-1, c), word[1:])
            if not any([is_down, is_right, is_left, is_up]):
                board[r][c] = word[0]
                return False
        else:
            return False                
        return True


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
