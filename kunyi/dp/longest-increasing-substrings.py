class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # O(n^2)
        # dp[] = [1] * len(nums), dp[i] - the length of LIS dp[0:(i+1)]
        if nums is None or len(nums) == 0:
            return 0 
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            tmp = dp[i]
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1 if dp[j] + 1 > tmp else tmp
            dp[i] = tmp

        return max(dp)
