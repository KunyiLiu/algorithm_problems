class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # bug: only visited once
        if board is None or len(board) == 0:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                exist = self.ifexist(board, word, 0, visited, i, j)
                if exist:
                    return True
        return False
    
    def ifexist(self, board, word, start, visited, i, j):
        # base case
        if start == len(word):
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return False
        if board[i][j] != word[start]:
            return False
        if visited[i][j]:
            return False
        visited[i][j] = True
        exist = self.ifexist(board, word, start + 1, visited, i+1, j) or self.ifexist(board, word, start + 1, visited, i-1, j) or self.ifexist(board, word, start + 1, visited, i, j + 1) or self.ifexist(board, word, start + 1, visited, i, j - 1)
        visited[i][j] = False # backtrack
        return exist
