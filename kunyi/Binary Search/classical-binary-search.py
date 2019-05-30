class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # sorted - premise
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid 
            elif nums[mid] == target:
                return mid
            else:
                start = mid 
                
        if nums[start] == target:
            return start 
        elif nums[end] == target:
            return end 
        
        return -1
