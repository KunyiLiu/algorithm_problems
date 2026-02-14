class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We do not need to track actual transactions because consecutive gains
        # are equivalent to holding through multiple days
        if not prices:
            return 0

        # catch every upward price
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])

        return profit
