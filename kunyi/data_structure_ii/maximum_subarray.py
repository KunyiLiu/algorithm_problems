class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # prefix sum + greedy 
        # max{aj - ai}, and j > i
        import sys
        prefix_sums = [0]
        tmp_sum = 0 
        for i in range(len(nums)):
            tmp_sum += nums[i]
            prefix_sums.append(tmp_sum)
            
        max_res = - sys.maxsize 
        min_prefix = prefix_sums[0]
        for i in range(1, len(nums) + 1):
            max_res = max(max_res, prefix_sums[i] - min_prefix)
            min_prefix = min(min_prefix, prefix_sums[i])
            
        return max_res
