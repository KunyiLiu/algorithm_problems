class Solution(object):
    def subsets(self, nums):
        res = []
        self.build(nums, res, [], 0)
        return res

    def build(self, nums, res, cur, start):
        res.append(cur)
        for i in range(start, len(nums)):
            self.build(nums, res, cur + [nums[i]], i + 1)


class Solution:
    def subsets(self, nums):
        res = []
        self.helper(nums, res, [], 0)
        return res 
    
    def helper(self, nums, res, subset, start_ind):
        res.append(subset[:])
        for i in range(start_ind, len(nums)):
            subset.append(nums[i])
            self.helper(nums, res, subset, i+1)
            subset.pop()
''' 
Success
Details 
Runtime: 40 ms, faster than 81.44% of Python3 online submissions for Subsets.
Memory Usage: 13.4 MB, less than 29.85% of Python3 online submissions for Subsets.
Next challenges:
Subsets II
Generalized Abbreviation
Letter Case Permutation
'''
