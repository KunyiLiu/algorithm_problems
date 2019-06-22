class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        profit, cur_min = 0, max(prices)
        for p in prices:
            if p < cur_min:
                cur_min = p
            profit = max(profit, p-cur_min)
        return profit 
'''
Success
Details
Runtime: 52 ms, faster than 40.33% of Python online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 12.5 MB, less than 6.04% of Python online submissions for Best Time to Buy and Sell Stock.
Next challenges:
Maximum Subarray
Best Time to Buy and Sell Stock II
Best Time to Buy and Sell Stock III
Best Time to Buy and Sell Stock IV
Best Time to Buy and Sell Stock with Cooldown
'''
