class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if len(board) == 0 or len(board[0]) == 0:
            return []
        self.m, self.n = len(board), len(board[0])
        self.deltaX = [-1, 0, 1, 0]
        self.deltaY = [0, -1, 0, 1]
        result = []
        for word in words:
            inds = self.get_first_position(word, board)
            if len(inds) == 0:
                continue
            for ind in inds:
                matched = self.helper(word[1:], board, [ind])
                if matched:
                    result.append(word)
                    break

        return result 
        
    def get_first_position(self, word, board):
        first_inds = []
        for i in range(self.m):
            for j in range(self.n):
                if word[0] == board[i][j]:
                    first_inds.append((i,j))
                    
        return first_inds
        
    def helper(self, word, board, last_inds):
        if len(word) == 0:
            return True 
        
        first_char = word[0]
        last_ind = last_inds[-1]
        x, y = last_ind[0], last_ind[1]
        for i in range(4):
            new_x, new_y = x + self.deltaX[i], y + self.deltaY[i]
            if 0 <= new_x < self.m and 0 <= new_y < self.n and first_char == board[new_x][new_y] and (new_x, new_y) not in last_inds:
                if self.helper(word[1:], board, last_inds + [(new_x, new_y)]):
                    return True 
                # do not return False yet, go to check another pair of (new_x, new_y)
                
        return False
