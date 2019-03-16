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
