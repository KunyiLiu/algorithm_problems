class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
            
        self.result = []
        self.nums = sorted(nums)
        self.dfs([], 0)
        return list(self.result)
       
    def dfs(self, subset, ind):
        self.result.append(subset[:])
        
        for i in range(ind, len(self.nums)):
            if i > ind and self.nums[i] == self.nums[i-1]:
                continue
            subset.append(self.nums[i])
            self.dfs(subset, i + 1)
            subset.pop()
            
        return 

##### 

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # introduce start_ind, dont look back 
        result = []
        # point 1. sorted 
        nums = sorted(nums)
        self.helper(nums, result, [], 0)
        return result 
        
    def helper(self, nums, result, subset, start_ind):
        result.append(subset[:])
        for i in range(start_ind, len(nums)):
            if i > start_ind and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.helper(nums, result, subset, i + 1)
            subset.pop()
