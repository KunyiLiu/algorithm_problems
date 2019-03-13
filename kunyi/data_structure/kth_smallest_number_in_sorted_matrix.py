
class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        if len(matrix) == 0 or matrix is None:
            return
        nums = [col for row in matrix for col in row]
        return self.mergesort(nums, 0, len(nums) - 1, k)
        
    def mergesort(self, nums, left, right, k):
        ind = self.partition(nums, left, right)
        if ind == k:
            return nums[ind - 1]
        if left < ind - 1:
            self.mergesort(nums, left, ind-1, k)
        if right > ind:
            self.mergesort(nums, ind, right, k)
        return nums[k - 1]
        
    def partition(self, nums, left, right):
        pivot_ind = left + (right - left) / 2
        pivot = nums[pivot_ind]
        nums[pivot_ind], nums[right] = nums[right], nums[pivot_ind]
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1 
                
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        return store_index + 1 
        
  ## heapsort 
  import heapq

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        if n == 0:
            return None
        
        m = len(matrix[0])
        if m == 0:
            return None
            
        minheap = [(matrix[0][0], 0, 0)]
        visited = set([0])
        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(minheap)
            if x + 1 < n and (x + 1) * m + y not in visited:
                heapq.heappush(minheap, (matrix[x + 1][y], x + 1, y))
                visited.add((x + 1) * m + y)
            if y + 1 < m and x * m + y + 1 not in visited:
                heapq.heappush(minheap, (matrix[x][y + 1], x, y + 1))
                visited.add(x * m + y + 1)

        return num
