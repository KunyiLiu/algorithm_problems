class Solution:
    """
    @param nums: an array of positive and negative integers
    @return: if there is a loop in this array
    """
    def circularArrayLoop(self, nums):
        # try Floyd's Cycle Detection 
        if len(nums) <= 1:
            return False 
        slow, fast = 0, 0 
        while True:
            slow = (slow + nums[slow]) % len(nums)
            fast = (fast + nums[fast]) % len(nums)
            fast = (fast + nums[fast]) % len(nums)
            if slow == fast:
                break
                
        head = slow 
        dup_count = 0
        while True:
            slow = (slow + nums[slow]) % len(nums)
            if nums[head] * nums[slow] <= 0:
                return False 
            if slow == head: 
                break 
            dup_count += 1 

        return dup_count >= 1
            
