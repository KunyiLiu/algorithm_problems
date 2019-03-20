class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the permutations that sum to target
    """
    def permute(self, num):
        # write your code here
        if num is None:
            return []
        if len(num) == 0:
            return [[]]
        self.result = []
        num = sorted((num))
        set1 = set()
        self.helper(num, set1, [])
        return self.result
    
    # return all permutations beginning with subset
    def helper(self, num, set, subset):
        length = len(num)
        if len(subset) == length:
            self.result.append(subset.copy())
            return
        for i in range(0, length):
            if num[i] in set:
                continue
            else:
                subset.append(num[i])
                set.add(num[i])
                self.helper(num, set, subset)
                set.remove(num[i])
                subset.pop()
