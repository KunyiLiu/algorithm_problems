class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        # binary search 
        result = None 
        for num in nums:
            if result == num:
                result = None 
            elif result is None:
                result = num 
                
        return result
