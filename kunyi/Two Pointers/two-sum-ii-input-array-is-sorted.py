class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1 
        while start < end:
            if nums[start] + nums[end] == target:
                return [start + 1, end + 1]
            elif nums[start] + nums[end] > target:
                end -= 1 
            else:
                start += 1 
                
        return [-1, -1]
