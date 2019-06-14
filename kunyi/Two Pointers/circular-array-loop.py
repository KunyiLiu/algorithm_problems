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

############### what if have multiple cycles like [3,1,2] ###############
class Solution:
    """
    @param nums: an array of positive and negative integers
    @return: if there is a loop in this array
    Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count.
    Use a slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. 
    If there is a loop (fast == slow), we return true, else if we meet element with different directions, 
    then the search fail, we set all elements along the way to 0. Because 0 is fail for sure so when later search 
    meet 0 we know the search will fail.
    """
    def get_index(self, i, nums):
        n = (i + nums[i]) % len(nums)
        return n if n >= 0 else n + len(nums)
        
    def circularArrayLoop(self, nums):
        # Write your code here
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            j, k = i, self.get_index(i, nums)
            while nums[k] * nums[i] > 0 and nums[self.get_index(k, nums)] * nums[i] > 0:
                if j == k:
                    if j == self.get_index(j, nums):
                        break
                    return True
                j = self.get_index(j, nums)
                k = self.get_index(self.get_index(k, nums), nums)
            j = i
            while nums[j] * nums[i] > 0:
                next = self.get_index(j, nums)
                nums[j] = 0
                j = next
                
        return False
