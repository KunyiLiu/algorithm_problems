class Solution:
    def permuteUnique(self, nums):
        res = []
        self.dfs(nums, [], set(), res)
        final_res = []
        for r in res:
            if r not in final_res:
                final_res.append(r)
        return final_res
    
    def dfs(self, nums, subset, visited, res):
        
        if len(subset) == len(nums):
            res.append(subset[:])
            return
        for i in range(len(nums)):
            if i not in visited:
                subset.append(nums[i])
                visited.add(i)
                self.dfs(nums, subset, visited, res)
                visited.remove(i)
                subset.pop()
            

'''
Success
Details 
Runtime: 1228 ms, faster than 5.04% of Python3 online submissions for Permutations II.
Memory Usage: 18.8 MB, less than 5.01% of Python3 online submissions for Permutations II.
Next challenges:
Next Permutation
Palindrome Permutation II
Number of Squareful Arrays

Related Topics: Backtracking
Similar Questions: Next Permutation, Permutations, Palindrome Permutation II, Number of Squareful Arrays
'''
