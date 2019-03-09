class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # use hash table to record the subarray sum from index 0 to current index
        # sum i - j = sum[j] - sum[i]
        if len(nums) == 0 or nums is None:
            return 
        sum_table = {0:0}
        tmp_sum = 0
        for i in range(len(nums)):
            tmp_sum = tmp_sum + nums[i]
            if tmp_sum - 0 in sum_table:
                return [sum_table[tmp_sum], i]
            sum_table[tmp_sum] = i + 1 
