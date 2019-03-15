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
