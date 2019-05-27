############## elems before stored_index/start < pivot, elems after that not sure ######
############# method 1. move all the elements < pivot to the left using stored index ###########
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        stored_index = 0 
        for i in range(len(nums)):
            if nums[i] < k:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1 
                
        return stored_index
        
############# mehod 2: from start, end converging to the mid, limiting the scope of unnormal elements ######################
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                # normal
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                # not normal - swap
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start
