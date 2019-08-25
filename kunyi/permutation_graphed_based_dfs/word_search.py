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

 ####### similar to color board #########
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # cannot use BFS - some of the pos might have been taken by other paths 
        # DFS - dfs(start_point, word), return boolean, if we can reach to the end if we start from the point 
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False 
            
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False] * n for _ in range(m)]
                    result = self.dfs(i, j, board, word, visited)
                    if result:
                        return True 
                        
        return False 
        
    def dfs(self, x, y, board, word, visited):
        m, n = len(board), len(board[0])
        if len(word) == 0:
            return True 
        
        if not(0 <= x < m and 0 <= y < n and visited[x][y] is False and board[x][y] == word[0]):
            return False 
        
        visited[x][y] = True 
        is_left = self.dfs(x-1, y, board, word[1:], visited)
        is_right = self.dfs(x+1, y, board, word[1:], visited)
        is_up = self.dfs(x, y-1, board, word[1:], visited)
        is_down = self.dfs(x, y+1, board, word[1:], visited)
        if not any([is_left, is_right, is_up, is_down]):
            # backtracking
            visited[x][y] = False 
            return False 
            
        return True
