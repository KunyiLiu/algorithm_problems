class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # q_cols each item represents the col of that item at the index 
        # [-1 -1 .. -1]
        # create a set to record chose columns (like permutation)
        if n == 0 or n is None:
            return []
            
        self.n = n 
        self.result = []
        self.dfs([], set())
        
        finals = []
        for i in self.result:
            finals.append(self.draw(i))
        
        return finals 
        
    # 1-n permutation     
    def dfs(self, subset, visited):
        if len(subset) == self.n:
            self.result.append(subset[:])
            return 
        
        for i in range(0, self.n):
            if i in visited or not self.is_safe(i, subset):
                continue
            
            subset.append(i)
            visited.add(i)
            self.dfs(subset, visited)
            visited.remove(i)
            subset.pop()
            
        return 
    
    def draw(self, array):
        tmp = [''.join(['.' if array[i] != j else 'Q' for j in range(self.n)]) for i in range(self.n)]
        return tmp
        
    def is_safe(self, col, subset):
        target_row = len(subset)
        for i in range(target_row):
            # check lower diagonal
            if subset[i] - i == col - target_row:
                return False
            # check upper diagonal
            if subset[i] + i == col + target_row:
                return False 
                
        return True 
