########## Time O(n) Space O(n) ######
class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # from_left, from_right 
        if nums is None or len(nums) == 1:
            return nums
            
        n = len(nums)
        from_left, from_right = nums[:], nums[:]
        for i in range(1, n):
            from_left[i] *= from_left[i-1]
            
        for i in range(n-2, -1, -1):
            from_right[i] *= from_right[i+1]
            
        result = []
        for i in range(n):
            if i == 0:
                result.append(from_right[1])
            elif i == n-1:
                result.append(from_left[n-2])
            else:
                result.append(from_left[i-1] * from_right[i+1])
            
        return result
        
##### Space: O(1) ###########
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for i in nums]
        nf = 1
        nb = 1
        length = len(nums)
        for i in range(length):
            result[i] *= nf
            nf *= nums[i]
            result[length-i-1] *= nb
            nb *= nums[length-i-1]
        return result
