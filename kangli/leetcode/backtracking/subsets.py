class Solution(object):
    def subsets(self, nums):
        res = []
        self.build(nums, res, [], 0)
        return res

    def build(self, nums, res, cur, start):
        res.append(cur)
        for i in range(start, len(nums)):
            self.build(nums, res, cur + [nums[i]], i + 1)

