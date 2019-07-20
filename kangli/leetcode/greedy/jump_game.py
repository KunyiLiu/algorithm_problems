class Solution:
    def canJump(self, nums):
        if len(nums) <= 1:
            return True
        jumps = 0
        for i in range(len(nums)):
            if jumps < i:
                return False
            if jumps >= len(nums)-1:
                return True
            jumps = max(jumps, i+nums[i])

#dp TEL


class Solution:
    def canJump(self, nums):
        state = [False]*len(nums)
        state[-1] = True
        i = len(nums)-2
        while i >= 0:
            for j in range(min(nums[i]+1, len(nums))):
                if state[j+i] == True:
                    state[i] = True
                    break
            i -= 1
        return state[0]

'''
75 / 75 test cases passed.
Status: Accepted
Runtime: 52 ms
Memory Usage: 14.5 MB
Your runtime beats 38.30 % of python3 submissions
Your memory usage beats 87.76 % of python3 submissions. 

Related Topics: Array, Greedy
Similar Question: Jump Game II
'''
