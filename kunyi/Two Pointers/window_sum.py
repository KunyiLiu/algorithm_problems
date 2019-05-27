class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        result = []
        if k < 1 or len(nums) < k:
            return result
        
        for i in range(len(nums) - k + 1):
            if i == 0:
                tmp_sum = sum(nums[i:(i+k)])
            else:
                tmp_sum = tmp_sum - nums[i-1] + nums[i+k-1]
                
            result.append(tmp_sum)
            
        return result
