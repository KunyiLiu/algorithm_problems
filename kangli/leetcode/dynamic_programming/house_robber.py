class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        cache = [0]*(len(nums))
        cache[0], cache[1] = nums[0], max(nums[0:2])
        for i in range(2, len(nums)):
            cache[i] = max(cache[i-1], cache[i-2]+nums[i])
        return cache[-1]
'''
Success
Details 
Runtime: 32 ms, faster than 9.92% of Python online submissions for House Robber.
Memory Usage: 11.7 MB, less than 5.29% of Python online submissions for House Robber.
Next challenges:
Maximum Product Subarray
House Robber II
Paint House
Paint Fence
House Robber III
Non-negative Integers without Consecutive Ones
Coin Path
Delete and Earn

Related Topics: Dynamic Programming
Similar Questions: Maximum Product Subarray
Medium
House Robber II
Medium
Paint House
Easy
Paint Fence
Easy
House Robber III
Medium
Non-negative Integers without Consecutive Ones
Hard
Coin Path
Hard
Delete and Earn

'''
