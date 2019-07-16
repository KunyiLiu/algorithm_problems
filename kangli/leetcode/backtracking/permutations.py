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
                
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res, set())
        return res 
    
    def dfs(self, nums, subset, res, visited):
      
        if len(subset) == len(nums):
            res.append(subset[:])
            return
        for n in nums:
            if n not in visited:
                subset.append(n)
                visited.add(n)
                self.dfs(nums, subset, res, visited)
                subset.pop()
                visited.remove(n)
'''
Success
Details 
Runtime: 44 ms, faster than 97.14% of Python3 online submissions for Permutations.
Memory Usage: 13.3 MB, less than 37.02% of Python3 online submissions for Permutations.
Next challenges:
Next Permutation
Permutations II
Permutation Sequence
Combinations
'''
