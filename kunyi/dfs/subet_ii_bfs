class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        from queue import Queue
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
         
        nums = sorted(nums)  
        queue = Queue()
        queue.put(([], -1))
        result = []
        
        while not queue.empty():
            subset, ind = queue.get()
            result.append(subset)
            
            for i in range(ind + 1, len(nums)):
                # not continue chosing like [1,2,2]
                if i > 0 and nums[i-1] == nums[i] and ind != i-1:
                    continue 
                # deep copy
                new_subset = subset + [nums[i]]
                queue.put((new_subset, i))
                
        return result 
