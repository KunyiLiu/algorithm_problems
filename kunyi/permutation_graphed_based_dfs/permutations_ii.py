class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums = sorted(nums)
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]
        self.result = []
        self.helper(nums, [])
        return self.result
    
    # find all permutations in nums beginning with tmp subset
    def helper(self, nums, tmp):
        if len(nums) == 0 :
            self.result.append(tmp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            sub1 = nums[i]
            sub2 = nums[:i] + nums[(i+1):]
            self.helper(sub2, tmp + [sub1])

 ######### 
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # since we have duplicate numbers, 
        # we cannot use set to check if the num has been put in subset
        # T(n) = O(n**2)
        # unique: i > 0, nums[i] == nums[i-1], sorted
        
        result = []
        if nums is None:
            return result
        # point 1. sort nums
        nums = sorted(nums)
        self.helper(nums, result, [])
        return result 
        
    def helper(self, nums, result, subset):
        if len(nums) == 0:
            # point 2. deep copy
            result.append(subset[:])
            return 
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            subset.append(nums[i])
            self.helper(nums[:i] + nums[(i+1):], result, subset)
            # point 3. backtrack
            subset.pop()
        
