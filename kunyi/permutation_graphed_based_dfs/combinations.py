class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # similar to start_ind, never look back
        # T(n) = Cnk = n* ..(n-k+1) / k!
        nums = [i+1 for i in range(n)]
        result = []
        self.dfs(nums, result, k, [], 0)
        return result 
        
    def dfs(self, nums, result, k, subset, start_ind):
        if len(subset) == k:
            result.append(subset[:])
            return
            
        for i in range(start_ind, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, result, k, subset, i + 1)
            subset.pop()
            
        return 
