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
