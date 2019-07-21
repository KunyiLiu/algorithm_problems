#### Time Complexity ######
##### T(n) = O(n) + T(n/2) = O(n) + O(n/2) + T(n/4) = O(n) ######
  // Returns the k-th smallest element of list within left..right inclusive
  // (i.e. left <= k <= right).
  // The search space within the array is changing for each round - but the list
  // is still the same size. Thus, k does not need to be updated with each round.
  function select(list, left, right, k)
     if left = right        // If the list contains only one element,
         return list[left]  // return that element
     pivotIndex  := ...     // select a pivotIndex between left and right,
                            // e.g., left + floor(rand() % (right - left + 1))
     pivotIndex  := partition(list, left, right, pivotIndex)
     // The pivot is in its final sorted position
     if k = pivotIndex
         return list[k]
     else if k < pivotIndex
         return select(list, left, pivotIndex - 1, k)
     else
         return select(list, pivotIndex + 1, right, k)
         
         
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthSmallestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, k-1)
        
    def partition(self, nums, start, end, k):
        """
        During the process, it's guaranteed start <= k <= end
        kth smallest (0 based) element
        """
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
                
        # nums[i] < pivot, i < l
        if l <= k:
            return self.partition(nums, l, end, k)
        else:
            return self.partition(nums, start, l-1, k)
            
        return nums[k]
