class NumArray(object):

    def __init__(self, nums):
        self.prefSums = nums
        for i in range(1, len(nums)):
            self.prefSums[i] = nums[i] + self.prefSums[i - 1]

    def sumRange(self, i, j):
        if i > 0:
            return self.prefSums[j] - self.prefSums[i - 1]
        else:
            return self.prefSums[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
'''
Success
Details 
Runtime: 72 ms, faster than 52.93% of Python online submissions for Range Sum Query - Immutable.
Memory Usage: 15.5 MB, less than 5.32% of Python online submissions for Range Sum Query - Immutable.
Next challenges:
Range Sum Query 2D - Immutable
Range Sum Query - Mutable
Maximum Size Subarray Sum Equals k

Related Topics: Dynamic Programming
Similar Questions:Range Sum Query 2D - Immutable
Range Sum Query - Mutable
Maximum Size Subarray Sum Equals k
'''
