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
