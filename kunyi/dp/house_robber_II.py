class Solution:
    def rob(self, nums: List[int]) -> int:
        # in circle, cannot rob both the first and last house
        # split: Rob houses from index 1 to n-1
        # Rob houses from index 0 to n-2
        if len(nums) == 1:
            return nums[0]

        rob1 = self.rob_helper(nums[1:])
        rob2 = self.rob_helper(nums[:-1])

        return max(rob1, rob2)

    
    def rob_helper(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
