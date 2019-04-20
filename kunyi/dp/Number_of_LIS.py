class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # len[i] 代表以第 i 个数结尾的最长上升子序列的长度。
        # cnt[i] 代表以第 i 个数结尾的最长上升子序列的个数。
        # len[i] = max(len[j] + 1), nums[j] < nums[i]。
        # cnt[i] = sum(cnt[j]), nums[j] < nums[i] and len[j] == len[i] - 1。
        # O(n^2)
        if nums is None or len(nums) == 0:
            return 0 
            
        n = len(nums)
        dp, cnt = [1] * n, [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1 
                        cnt[i] = cnt[j]
                
          
        max_height = max(dp)
        result = 0 
        for i in range(n):
            if dp[i] == max_height:
                result += cnt[i]
            
        return result
