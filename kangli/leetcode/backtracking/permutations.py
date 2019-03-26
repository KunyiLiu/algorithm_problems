class Solution:
    def permute(self, nums):

        def dfs(nums, count, cur, res):
            if count == len(nums):
                res.append(cur)
            else:
                for n in nums:
                    if n not in cur:
                        dfs(nums, count + 1, cur + [n], res)

        res = []
        dfs(nums, 0, [], res)
        return res

#slight variation written during review

class Solution(object):
    def permute(self, nums):
        res = []
        self.build([], res, nums)
        return res

    def build(self, temp, res, nums):
        if len(temp) == len(nums):
            res.append(temp[:])
            start = 0
            return
        for n in nums:
            if n not in temp:
                temp.append(n)
                self.build(temp, res, nums)
                temp.pop()
