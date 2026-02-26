class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] - the max money you can rob when reaching to i index house
        # base case: dp[0] = nums[0], dp[1] = max(nums[1], nums[0]) (without alert)
        # inference: dp[i] = max(dp[i-2] + nums[i], dp[i - 1]), i >= 2
        # result: dp[n - 1]
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i - 1])

        return dp[n-1]
        
