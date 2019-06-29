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
