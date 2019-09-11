class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # (nums[i] - nums[i-1]) *  int(i%2 == 1) >= 0 
        # if not meet the inequality, rotate the nums[i-1] with nums[i]
        # O(n)
        # edge cases: [3, 3, 3, 3]
        #  [5, 4, 3, 2]
        # [4, 1, 3, 2]
        if nums is None or len(nums) <= 1:
            return nums 
        
        for i in range(1, len(nums)):
            multiplier = 1 if i % 2 == 1 else -1
            if (nums[i] - nums[i-1]) * multiplier < 0:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                
        return nums 
