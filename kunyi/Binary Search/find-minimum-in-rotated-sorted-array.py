class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # premise: non-descending
        # first position <= last number 
        # not the first position <= the very first number, like [2,1]
        if nums is None or len(nums) == 0:
            return
        
        start, end = 0, len(nums) - 1 
        last_elem = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > last_elem:
                start = mid
            elif nums[mid] < last_elem:
                end = mid 
            else:
                end = mid 
                
        if nums[start] <= last_elem:
            return nums[start]
        if nums[end] <= last_elem:
            return nums[end]
            
        return
