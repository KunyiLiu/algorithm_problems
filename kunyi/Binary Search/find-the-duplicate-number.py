##########  Method 1. sort - Time O(nlogn), Space O(n)  ############
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # for loop, if nums[i] can be found in 
        # nums[i+1, ..., n-1]
        # O(nlogn)
        if nums is None or len(nums) <= 1:
            return -1 
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return nums[i]
                
        return -1
        
#####  Method 2. set - Time O(n), Space O(n) ########

#####  Method 3. Floyd Cycle Detection ######
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # Floyd Cycle Detection 
        if nums is None or len(nums) == 0:
            return - 1 
            
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        
        # find the entrance to the cycle 
        # x == z 
        head = nums[0]
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        
        return head
