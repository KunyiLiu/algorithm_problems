########################## TIME LIMIT EXCEED ####################
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        m = len(nums)
        self.prefix_sum = [0] * (m+1)
        for i in range(m):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]
        self.nums = nums
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        for j in range(i, len(self.nums)):
            self.prefix_sum[j+1] += diff
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum[j+1] - self.prefix_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


####################### BINARY INDEXED TREE ######################################
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # 一道维护序列"单点修改, 区间查询"的模板题.
        # 可以用树状数组, 区间树, 平衡树等数据结构解决.
        # log(n) for update and get_prefix_sum, construct needs nlog(n)
        m = len(nums)
        self.bit = [0] * (m+1)
        self.nums = nums
        for i in range(m):
            self.add(i, self.nums[i])
        
    def lowbit(self, x):
        # 2's component of x
        return x & (-x)
        
    def add(self, i, val):
        ind = i + 1 
        while ind <= len(self.nums):
            self.bit[ind] += val
            ind += self.lowbit(ind)
    

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.add(i, diff)
            
    def get_prefix_sum(self, ind):
        tmp_sum = 0
        ind += 1 
        while ind > 0:
            tmp_sum += self.bit[ind]
            ind -= self.lowbit(ind)
        return tmp_sum
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_prefix_sum(j) - self.get_prefix_sum(i-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
