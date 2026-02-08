# https://neetcode.io/problems/find-duplicate-integer/question
# A linked list cycle problem, since the elem value is [1, n], think of it as the next index destination it is pointing to
# Use Floyd's Cycle Detection. Time: O(n), Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floy cycle issue, fast - slow pointer
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break

        return slow
            
        
