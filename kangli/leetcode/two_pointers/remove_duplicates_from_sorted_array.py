class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[cur] = nums[i]
                cur += 1 
        return cur
        

'''
Success
Details 
Runtime: 96 ms, faster than 77.15% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.4 MB, less than 5.01% of Python3 online submissions for Remove Duplicates from Sorted Array.
Next challenges: Remove Element, Remove Duplicates from Sorted Array II

Related Topics: Array, Two Pointers
'''
