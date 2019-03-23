class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        chess = [] # record the Q col of each row
        result = []
        self.dfs(n, chess, result)
        return len(result)
        
    def dfs(self, n, chess, result):
        if len(chess) == n:
            result.append(self.draw(chess, n))
            return 
        
        for col in range(n):
            if self.is_safe(col, chess, n):
                chess.append(col)
                self.dfs(n, chess, result)
                chess.pop()
                
                
    def is_safe(self, col, chess, n):
        row = len(chess)
        # test Q location is (row, col)
        # check if test Q is sharing the same col  (can be reversed)
        if col in chess:
            return False
        for i in range(row):
            # current Q(i, chess[i])
            # lower diagonal
            if chess[i] - i == col - row:
                return False
            # upper
            if chess[i] + i == col + row:
                return False
        return True
        
    def draw(self, chess, n):
        tmp = [''.join(['Q' if col == chess[row] else '.' for col in range(n)]) for row in range(n)]
        return tmp
