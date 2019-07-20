class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        self.build([], res, 0, sorted(nums))
        return res

    def build(self, temp, res, start, nums):
        res.append(temp)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.build(temp + [nums[i]], res, i + 1, nums)
'''
Success
Details
Runtime: 28 ms, faster than 100.00% of Python online submissions for Subsets II.
Memory Usage: 11 MB, less than 26.32% of Python online submissions for Subsets II.

Next Challenges: Merge Sorted Array
Contains Duplicate
Wiggle Sort

Related Topics: Array, Backtracking
Similar Questions: subsets
'''


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums = sorted(nums)
        self.helper(nums, res, [], 0)
        return res 
    
    def helper(self, nums, res, subset, start_ind):
        res.append(subset[:])
        for i in range(start_ind, len(nums)):
            if i > start_ind and nums[i] == nums[i-1]:
                continue 
            subset.append(nums[i])
            self.helper(nums, res, subset, i+1)
            subset.pop()
            

'''
Success
Details 
Runtime: 40 ms, faster than 96.97% of Python3 online submissions for Subsets II.
Memory Usage: 13.2 MB, less than 75.04% of Python3 online submissions for Subsets II.
Next challenges:
Word Ladder II
K-diff Pairs in an Array
Unique Paths III
Show off your acceptance:
'''
