class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # partition to 2 parts
        # first partition: [0, not 0]
        # second partition: not 0: [1, 2]
        # O(n) time, constant space
        if nums is None or len(nums) == 0:
            return []
        
        start, end = 0, len(nums) - 1  
        for target in [0,1]:
            stored_ind = self.partition_array(nums, start, end, target)
            start = stored_ind
            
        return nums
        
    def partition_array(self, nums, start, end, target):
        while start <= end:
            while start <= end and nums[start] == target:
                start += 1 
            while start <= end and nums[end] != target:
                end -= 1 
                
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1 
                end -= 1 
        
        return start 
        
 ###########  method 2 ############
 # three pointers - index, left, right
 # index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管
 class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1

        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1
            elif A[index] == 1:
                index += 1
            else:
                A[right], A[index] = A[index], A[right]
                right -= 1
