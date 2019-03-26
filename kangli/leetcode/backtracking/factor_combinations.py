class Solution:
    def getFactors(self, n):

        if n == 1:
            return []
        res = []

        def dfs(path, step, target):
            if len(path) > 0:
                res.append(path + [target])
            for i in range(step, int(math.sqrt(target)) + 1):
                if target % i == 0:
                    dfs(path + [i], i, target // i)

        dfs([], 2, n)
        return res

'''
Success
Details 
Runtime: 20 ms, faster than 95.55% of Python online submissions for Factor Combinations.
Memory Usage: 12 MB, less than 7.14% of Python online submissions for Factor Combinations.
Next challenges: Permutations II
Word Ladder II
Word Squares

Related Topics: Backtracking
similar questions: Combination Sum
'''
