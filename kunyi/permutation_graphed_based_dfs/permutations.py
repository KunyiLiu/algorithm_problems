#####  use visited[n] to ensure chosen element not being picked again ###

class Solution:
    # Time complexity/Space: O(n*n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False



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
