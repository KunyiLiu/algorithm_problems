class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # n - two sum using hash_table: val: ind 
        count = 0 
        count_dict = {0: -1}  # count: ind 
        result = 0
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1 
            elif num == 1:
                count += 1 
            
            if count in count_dict:
                result = max(result, i - count_dict[count])
            else:
                # keep the old ind if count already exists
                count_dict[count] = i
                
        return result
