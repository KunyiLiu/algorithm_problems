class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # how to deal with nums[i] == nums[i-1]
        if nums is None or len(nums) <= 1:
            return nums 
        
        # quick sort [4, 5, 5, 6], [1,1,1,1, 4,5,6]
        # [5, 6, 4, 5 ], [1, 6, 1, 5, 1, 4]
        # time - O(nlogn); space - O(n)
        n = len(nums)
        self.quick_sort(nums, 0, n-1)
        
        new_nums = nums[:]
        small, large = (n -1) // 2, n - 1 
    
        for i in range(0, n, 2):
            print(small)
            nums[i] = new_nums[small]
            small -= 1 
            
        for i in range(1, n, 2):
            nums[i] = new_nums[large]
            large -= 1 
            
        
    def quick_sort(self, nums, start, end):
        if start >= end:
            return 
        
        l, r = start, end 
        pivot = nums[start]
        
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1 
                
            while l <= r and nums[r] > pivot:
                r -= 1 
                
            if l<= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
                
        # get  nums[:l] <= pivot
        self.quick_sort(nums, start, l-1)
        self.quick_sort(nums, l, end)
        
### find median 
### put the num > median 
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # how to deal with nums[i] == nums[i-1]
        if nums is None or len(nums) <= 1:
            return nums 

        n = len(nums)
        median = self.find_median(nums, 0, n-1, (n-1) // 2)
        
        ans = [median] * n 
        # small from large to small 
        # large from small to large
        small, large = n - 2 if n % 2 == 0 else n - 1, 1

        for i in range(n):
            if nums[i] > median:
                ans[large] = nums[i]
                large += 2 
            elif nums[i] < median:
                ans[small] = nums[i]
                small -= 2 
                
        print(nums, ans, median)
            
        for i in range(n):
            nums[i] = ans[i]
        
            
        
    def find_median(self, nums, start, end, kth):
        if start >= end:
            return nums[start]
        
        l, r = start, end 
        pivot = nums[start]
        
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1 
                
            while l <= r and nums[r] > pivot:
                r -= 1 
                
            if l<= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
                
        # get  nums[:l] <= pivot
        if kth <= l-1:
            return self.find_median(nums, start, l-1, kth)
        else:
            return self.find_median(nums, l, end, kth)
            
