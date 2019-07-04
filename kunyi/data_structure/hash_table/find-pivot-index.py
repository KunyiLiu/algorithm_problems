##### subarray ######
class Solution:
    """
    @param nums: an array
    @return: the "pivot" index of this array
    """
    def pivotIndex(self, nums):
        # get the whole sum, hash table sub_sum
        # for loop: sum - sub_sum[3] = 11 == sub_sum[3-1]
        # O(n)
        
        sub_sum = {}
        whole_sum = sum(nums)
        for i in range(len(nums)):
            if i == 0:
                sub_sum[i] = nums[i]
                if whole_sum - sub_sum[i] == 0:
                    return i
            else:
                sub_sum[i] = sub_sum[i-1] + nums[i]
                if whole_sum - sub_sum[i] == sub_sum[i-1]:
                    return i 
                    
        return -1
        
###### partition to left and right ####
# 从左向右枚举中心索引
class Solution(object):
    def pivotIndex(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
