class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # day 0 base states
        hold = -prices[0]   # best profit if we hold a stock at end of day 0
        sold = 0            # best profit if we sold today (day 0) — impossible but 0 base
        rest = 0            # best profit if we rest (not holding) at end of day 0

        for i in range(1, len(prices)):
            prev_hold, prev_sold, prev_rest = hold, sold, rest

            # either keep holding, or buy today (must have been resting yesterday)
            hold = max(prev_hold, prev_rest - prices[i])

            # if we sell today, we must have been holding until yesterday
            sold = prev_hold + prices[i]

            # rest = max(previous rest, or we just came from a sell yesterday)
            rest = max(prev_rest, prev_sold)

        # final profit is when we are not holding a stock (either just sold or resting)
        return max(sold, rest)
