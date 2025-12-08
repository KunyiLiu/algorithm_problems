class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # use partition sort 
        # time complexity: O(nlogn), worst case O(n^2), more closer to nlogn with the use of median of tree pivot technique,
        # ensuing nums[start] <= nums[mid] <= nums[end] before partitioning.
        # space: O(logn) for stacks
        n = len(nums)
        if n <= 1:
            return nums

        self.quick_sort(nums, 0, n-1)
        return nums
    
    def quick_sort(self, nums, start, end):
        if start >= end:
            return

        pivot_ind = self.quick_select(nums, start, end)
        self.quick_sort(nums, start, pivot_ind - 1)
        self.quick_sort(nums, pivot_ind + 1, end)

    def quick_select(self, nums, start, end): 
       # ----- median-of-three pivot selection -----
        mid = start + (end - start) // 2
        # sort start, mid, end and pick mid as pivot
        if nums[start] > nums[end]:
            nums[start], nums[end] = nums[end], nums[start]
        if nums[mid] > nums[end]:
            nums[mid], nums[end] = nums[end], nums[mid]
        if nums[start] > nums[mid]:
            nums[start], nums[mid] = nums[mid], nums[start]

        pivot_ind = start
        pivot = nums[start]
        start += 1
        
        while start <= end:
            while start <= end and nums[start] <= pivot:
                start += 1

            while start <= end and nums[end] > pivot:
                end -= 1 

            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1 
                end -= 1

        nums[pivot_ind], nums[end] = nums[end], nums[pivot_ind]
        return end
