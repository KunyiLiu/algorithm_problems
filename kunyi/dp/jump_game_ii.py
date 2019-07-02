class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # Greedy O(n)
        if A is None or len(A) == 0:
            return -1 
            
        end, start, jumps = 0, 0, 0 
        n = len(A)
        farthest = 0
        while True:
            if farthest >= n - 1:
                break 
            jumps += 1 
            # 0->0  1 -> farthest, 2-> farthest ..
            for i in range(start, end+1):
                if A[i] + i > farthest:
                    farthest = A[i] + i 
            
            start += 1 
            end = farthest
        
        
        return jumps
        
        
 class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # dp[i] - the min jump steps from 0 to i 
        # O(n^2) - dp
        if A is None or len(A) == 0:
            return -1 
            
        n = len(A)
        dp = [-1] * n 
        dp[0] = 0 
        
        for i in range(1, n):
            for j in range(0, i):
                if dp[j] >= 0 and j + A[j] >= i: 
                    dp[i] = min(dp[i], dp[j] + 1) if dp[i] >=0 else dp[j] + 1
        
        return dp[n-1]
    
############## greedy based on jump_game
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # Greedy O(n)
        if A is None or len(A) <= 1:
            return 0 
            
        end, start, jumps = 0, 0, 1
        n = len(A)
        farthest = A[0]
        
        for i in range(1, n):
            if farthest >= n - 1:
                break 
            # i - start, farthest - end, A[i] - steps
            if i <= farthest and A[i] + i > farthest:
                farthest = A[i] + i
                jumps += 1
        
        return jumps
