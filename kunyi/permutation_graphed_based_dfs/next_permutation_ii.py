class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # 例如[1,1,1,2,2,3]，排列数为6!÷(3!×2!×1!)。
        n = len(nums)
        # corner case  
        if n < 2:
            return nums 
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        # find the left ind of the descending sublit 
        else:
            self.inplace_reverse(nums, 0, n-1)
            return nums
            
        for j in range(n-1, i, -1):
            if nums[j] > nums[i]:
                break 
            
        nums[i], nums[j] = nums[j], nums[i]
        
        self.inplace_reverse(nums, i+1, n-1)
        
        return nums 
        
    def inplace_reverse(self, nums, i, j):
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1 
            j -= 1 
