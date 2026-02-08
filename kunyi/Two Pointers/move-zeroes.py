###################  store index ###################
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        count = 0
        n = len(nums)
        if n == 0 or nums is None:
            return []
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        # count - the index of the first 0
        for i in range(count, n):
            nums[i] = 0
        return nums


################ pointer for zero and non-zero ###############
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # partition - not keeping relative order 
        # same direction pointers
        zero, non_zero = 0, 0 
        while zero < len(nums) and non_zero < len(nums):
            if nums[zero] != 0:
                zero += 1 
                continue
            if nums[non_zero] == 0:
                non_zero += 1
                continue
                
            if zero < non_zero:
                nums[non_zero], nums[zero] = nums[zero], nums[non_zero]
                zero += 1
            
            non_zero += 1 
            
        return nums

#### partition sorting #######
class Solution:
    def move_zeroes(self.nums):
        # l: boundary for non-zeroes (the "Left" bucket)
        # i: explorer pointer
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current non-zero to the left boundary
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
