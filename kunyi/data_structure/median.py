class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # O(n)
        if nums is None or len(nums) == 0:
            return 
        
        median = self.find_median(nums, 0, len(nums) - 1, (len(nums) - 1)// 2)
        return median 
        
    def find_median(self, nums, start, end, kth):
        if start == end:
            return nums[start]
        l, r = start, end 
        pivot = nums[start]
        
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1 
                
            while l <= r and nums[r] > pivot:
                r -= 1 
                
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
        
        # kth <= l - 1 
        # kth >= l
        if l <= kth:
            return self.find_median(nums, l, end, kth)
        else:
            return self.find_median(nums, start, l-1, kth)
        
