class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use dfs with memo -> Top down
        # unlike combination sum, which does not allow [2, 3, 3] and [3, 3, 2],
        # coin change does not care about ordering
        # Time complexity: O(#amount * #coins), Space: O(#amount)->memo
        result = self.dfs(coins, {}, amount)

        return result if result < float('inf') else -1

    def dfs(self, coins, memo, target):
        if target == 0:
            return 0

        if target in memo:
            return memo[target]

        res = float('inf')
        for coin in coins:
            if coin > target:
                continue

            res = min(1 + self.dfs(coins, memo, target - coin), res)

        memo[target] = res

        return res


###### DP bottom up #####
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] - minimum of coins to get to i
        # base: dp[0] = 0
        # inference: dp[i] = min(dp[i - c] + 1, dp[i]) for every coin
        # result: dp[amount]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue

                dp[i] = min(dp[i - coin] + 1, dp[i])

        return dp[amount] if dp[amount] < float('inf') else -1
        
