class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # sum_dict = {sub_sum: ind} check sub_sum - k in sum_dict 
        # initial {0: -1}
        # {0: -1, -2: 0, -3: 1, -1: 2} -1 - (-2) = k 
        # note that if sub_sum in sum_dict not updated the ind 
        sub_sum = 0 
        sum_dict = {0: -1}
        result = 0 
        for i, num in enumerate(nums):
            sub_sum += num 
            if sub_sum - k in sum_dict:
                result = max(result, i - sum_dict[sub_sum - k])
            
            if sub_sum not in sum_dict:
                sum_dict[sub_sum] = i 
                
        return result 
