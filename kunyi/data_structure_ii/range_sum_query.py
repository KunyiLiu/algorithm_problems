class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # prefix_sum 
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j+1] - self.prefix_sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
