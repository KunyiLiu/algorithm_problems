
####### NEETCODE ######

class MedianFinder:
    # when it comes to median problem, there is always left/right partition issue
    # left partition  - maxHeap (n//2 or n//2 + 1 elements); right partition - minHeap (n//2)
    # median - if even, maxHeap[0] + minHeap[0] / 2; odd, maxHeap[0]
    # left (max-heap) stores the smaller half of the elements, and tries to put the largest from the smaller half to the top
    import heapq
    def __init__(self):
        # care for the largest of left_part -> max_heap
        self.left_part = []
        # care for the smallest of right_part -> min_heap
        self.right_part = []
        
    def addNum(self, num: int) -> None:
        """
        Insert into one of the heaps:
          - If num <= current median → goes to left (max-heap)
          - Otherwise → goes to right
        Then rebalance to maintain heap size constraints.
        """
        # Handle first value gracefully
        if not self.left_part and not self.right_part:
            heapq.heappush(self.left_part, -num)
            return

        median = self.findMedian()

        # Decide which heap to push into
        if num <= median:
            heapq.heappush(self.left_part, -num)
        else:
            heapq.heappush(self.right_part, num)

        # Rebalance: left can only exceed right by 1
        if len(self.left_part) > len(self.right_part) + 1:
            heapq.heappush(self.right_part, -heapq.heappop(self.left_part))

        # Or right cannot have more than left
        if len(self.right_part) > len(self.left_part):
            heapq.heappush(self.left_part, -heapq.heappop(self.right_part))
        
    def findMedian(self) -> float:
        capacity = len(self.left_part) + len(self.right_part)
        if capacity == 0:
            return float("-inf")
        if capacity % 2:
            return -self.left_part[0]
        else:
            return (-self.left_part[0] + self.right_part[0])/2
        
        




########
import heapq
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # maxheap - left part nums 
        # minheap - right part nums 
        # median - maxheap[0]
        self.maxheap, self.minheap = [-nums[0]], []
        self.nums = nums
        result = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            self.add_num(num)
            result.append(self.median)
        return result 
        
    @property 
    def median(self):
        # if len(self.maxheap) == 0:
        #     return self.nums[0]
        return -self.maxheap[0]
        
    def add_num(self, num):
        if num > self.median:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
            
        # balance
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
