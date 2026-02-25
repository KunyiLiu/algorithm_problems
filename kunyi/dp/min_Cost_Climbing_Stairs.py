class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[n - 1] - the total cost to take to reach to n - 1 index
        # base: dp[0] = 0, dp[1] = 0
        # inference: dp[i] = min(dp[i - 1] + cost[i - 1], 
        # dp[i-2] + cost[i - 2])
        # Note! The top of the staircase is at index n (one step past the last stair), not at index n-1. 
        n = len(cost)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]
        
