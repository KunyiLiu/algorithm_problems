class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # O(n^2)
        # dp[i] = lis(divirative elems)
        if nums is None or len(nums) == 0:
            return []
            
        nums = sorted(nums)
        dp = {}
        for i in range(len(nums)):
            dp[i] = list()
        dp[0].append(nums[0])
        
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
                    
        
        result = []
        for i in range(len(nums)):
            result = dp[i] if len(dp[i]) > len(result) else result
            
        return result 
