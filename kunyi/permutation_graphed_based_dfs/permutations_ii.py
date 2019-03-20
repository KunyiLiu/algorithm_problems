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
