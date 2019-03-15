class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        self.result = []
        self.nums = sorted(nums)
        
        self.dfs([], 0)
        return self.result
    
    
    # def 1: find all the subsets beginning from subset in nums, 
    # start_index is to make sure deduplication
    def dfs(self, subset, start_index):
        self.result.append(subset[:])
            
        for i in range(start_index, len(self.nums)):
            subset.append(self.nums[i])
            self.dfs(subset, i + 1 )
            
            subset.pop()
            
        return 
    
    # def 2: starting with subset, combined with the nums at the start_index
    def dfs(self, subset, start_index):
        if start_index == len(self.nums):
            self.result.append(subset[:])
            return 
        
        subset.append(self.nums[start_index])
        self.dfs(subset, start_index + 1)
        
        subset.pop()
        self.dfs(subset, start_index + 1)
