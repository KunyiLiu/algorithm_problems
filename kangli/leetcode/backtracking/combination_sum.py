class Solution(object):
    def combinationSum(self, candidates, target):
        solution = []
        self.dfs([], solution, 0, candidates, target)
        return solution

    def dfs(self, temp, res, start, candidates, target):
        if target < 0:
            return
        elif target == 0:
            res.append(temp[:])
        for i in range(start, len(candidates)):
            temp.append(candidates[i])
            self.dfs(temp, res, i, candidates, target - candidates[i])
            temp.pop()


'''
Success
Runtime: 92 ms, faster than 46.98% of Python online submissions for Combination Sum.
Memory Usage: 10.7 MB, less than 68.25% of Python online submissions for Combination Sum.

Details:
168 / 168 test cases passed.
Status: Accepted
Runtime: 92 ms
Memory Usage: 10.7 MB

Related Topics: Array, Backtracking

Similar Questions:
Letter Combinations of a Phone Number
Medium
Combination Sum II
Medium
Combinations
Medium
Combination Sum III
Medium
Factor Combinations
Medium
Combination Sum IV
Medium
'''
