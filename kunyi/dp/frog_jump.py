class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # compare with LIS, dp not record the direct result
        # dp {}
        # dp[stone] set, record steps to stone.
        # inference
        # jump k - 1 to stone + k - 1:dp[stone + k - 1].add(k - 1)
        # jump k to stone + k:dp[stone + k].add(k)
        # jump k + 1 to stone + k + 1:dp[stone + k + 1].add(k + 1)
        # see if len(dp[nth stone]) > 0 
        dp = {}
        for stone in stones:
            dp[stone] = set([])
            
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                # forward
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k-1)
                    
                if stone + k in dp:
                    dp[stone + k].add(k)
                    
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k+1)
                    
                    
        return len(dp[stones[-1]]) > 0
    
    
###### 
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # def:  dp[i] - if frog can jump from 0 to index i 
        # initial: dp[0] = True, dp[1] = True if stones[1] == 1 
        # inference: dp[i] = True if dp[k] == True and stones(i) - stones(k) in steps[k]
        # where k < i 
        # result: dp[n-1]
        # O(n^2)
        
        n = len(stones)
        dp = [False] * n 
        dp[0] = True
        steps = {}
        for i in range(n):
            if i == 0:
                steps[i] = set([0])
            else:
                steps[i] = set([])
                
        for i in range(1, n):
            for j in range(i):
                if dp[j] is False:
                    continue
                tmp_k = stones[i] - stones[j]
                if tmp_k in steps[j] or tmp_k - 1 in steps[j] or tmp_k + 1 in steps[j]:
                    dp[i] = True 
                    steps[i].add(tmp_k)
                    
        return dp[n-1]
