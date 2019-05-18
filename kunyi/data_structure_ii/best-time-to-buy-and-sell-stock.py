class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        # greedy: s = {a1...an}, get max({aj - ai}) and j > i 
        import sys
        max_res = 0
        min_prefix = prices[0] 
        for i in range(1, len(prices)):
            max_res = max(max_res, prices[i] - min_prefix)
            min_prefix = min(min_prefix, prices[i])
            
        return max_res
