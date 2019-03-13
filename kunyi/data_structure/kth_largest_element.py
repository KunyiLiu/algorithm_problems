class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        len1 = len(nums)
        num = self.mergesort(nums, 0, len1-1, len1 - n + 1)
        return num 
        
    def mergesort(self, nums, left, right, n):  
        index = self.partition(nums, left, right)
        if index == n:
            return nums[index - 1]
        if left < index - 1:
            self.mergesort(nums, left, index - 1, n)
        if right > index:
            self.mergesort(nums, index, right, n)
        return nums[n - 1]
    
    def partition(self, nums, left, right):
        pivot_ind = left + (right - left) / 2
        pivot = nums[pivot_ind]
        store_index = left  # partition less and more 
        # move pivot to the end 
        nums[pivot_ind], nums[right] = nums[right], nums[pivot_ind]
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_index] = nums[store_index],nums[i]
                store_index += 1
        
        nums[right], nums[store_index] = nums[store_index], nums[right]
        
        # actual order of the pivot
        return store_index + 1
            
