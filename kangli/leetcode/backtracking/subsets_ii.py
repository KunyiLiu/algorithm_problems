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
