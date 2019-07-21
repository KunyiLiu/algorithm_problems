##############       find the last position that satisfies is_larger_than_last   ##############
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1 
            
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            # find the last position that satisfies is_larger_than_last
            if self.is_larger_than_last(nums, mid):
                start = mid
            else:
                end = mid 
                
        if self.is_local_top(nums, end):
            return nums[end]
        
        if self.is_local_top(nums, start):
            return nums[start]
            
        return -1 
        
    def is_local_top(self, array, ind):
        if len(array) == 1:
            return True
        if ind <= 0:
            return array[ind] >= array[ind+1]
        if ind >= len(array) - 1:
            return array[ind] >= array[ind-1]
            
        return array[ind] >= array[ind+1] and array[ind] >= array[ind-1]
        
    def is_larger_than_last(self, array, ind):
        if ind <= 0:
            return True 
        
        return array[ind] >= array[ind-1]
        
######  Method 2. the first position satisfies is_larget_than_the next ######
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1 
            
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            # mid < end definitely
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid 
                
        return max(nums[start], nums[end])
