class Solution(object):
    def combinationSum2(self, candidates, target):
        solution = []
        self.dfs(solution, [], 0, sorted(candidates), target)
        return solution

    def dfs(self, res, temp, start, candidates, target):
        if target < 0:
            return
        elif target == 0:
            res.append(temp[:])
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            temp.append(candidates[i])
            self.dfs(res, temp, i + 1, candidates, target - candidates[i])
            temp.pop()

'''
Success
Details 
Runtime: 96 ms, faster than 37.34% of Python online submissions for Combination Sum II.
Memory Usage: 10.9 MB, less than 17.84% of Python online submissions for Combination Sum II.
172 / 172 test cases passed.
Status: Accepted
Runtime: 96 ms
Memory Usage: 10.9 MB

Next challenges:
Third Maximum Number
Find All Numbers Disappeared in an Array
Maximum Width Ramp

Related topics: Array, Backtracking
Similar Questions: Combination Sum
'''
