class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # Greedy: to see if it is within farthest
        if A is None or len(A) == 0:
            return False 
            
        farthest = A[0]
        n = len(A)
        for i in range(1, n):
            if i <= farthest and i + A[i] > farthest:
                farthest = i + A[i]
                
        return farthest >= n-1
        
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # dp [i] - if 0 can jump to i 
        n = len(A)
        dp = [False] * n 
        dp[0] = True
        for i in range(1, n):
            for j in range(0, i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True 
                    break 
   
        return dp[n-1]
