######### heap ##############
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # heap - O(nlogk)
        # partition O(n)
        import heapq  # min heap 
        heap = []
        for num in nums:
            # top k largest elements, from small to large
            # if num < heap[0], push and then pop immediately
            if len(heap) == n and num > heap[0]:
                heapq.heappushpop(heap, num)
            elif len(heap) < n:
                heapq.heappush(heap, num)
         
        result = heapq.heappop(heap)
        
        return result 
        
####### partition ###################
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        kth smallest (0 based) element
        """
        if start == end:
            return nums[start]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            # partition array's not move itself pivot
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        # left is not bigger than right
        # print(left, right, k, nums, nums[left], pivot, start, end)

        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)
        
        return nums[k]
 
########### partition #############
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # heap - O(nlogk)
        # partition O(n)
        k = len(nums) - n 
        result = self.mergesort(nums, 0, len(nums) - 1, k)
        return result 
        
    def mergesort(self, nums, left, right, k):
        pivot_index = self.partition_array(nums, left, right)
        if pivot_index == k:
            return nums[k]
        elif pivot_index < k:
            return self.mergesort(nums, pivot_index + 1, right, k)
        elif pivot_index > k:
            return self.mergesort(nums, left, pivot_index - 1, k)
            
    
    def partition_array(self, nums, start, end):
        pivot_ind, pivot = end, nums[end]
        stored_ind = start
        for i in range(start, end):
            if nums[i] < pivot:
                nums[i], nums[stored_ind] = nums[stored_ind], nums[i]
                stored_ind += 1 
        
        # exchange with the right ind         
        nums[stored_ind], nums[pivot_ind] = nums[pivot_ind], nums[stored_ind]
        
        return stored_ind
        
    
