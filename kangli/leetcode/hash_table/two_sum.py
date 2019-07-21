class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                return [d[n], i]
            else:
                d[target-n] = i 
        return -1 

'''
Success
Details 
Runtime: 40 ms, faster than 76.54% of Python3 online submissions for Two Sum.
Memory Usage: 14.5 MB, less than 22.10% of Python3 online submissions for Two Sum.
Next challenges:
3Sum
4Sum
Two Sum II - Input array is sorted
Two Sum III - Data structure design
Two Sum IV - Input is a BST

Related Topics: Array, Hash Table
Similar Questions: 3sum, 4Sum, Two Sum II - Input array is sorted, 
Two Sum III - Data structure design, Subarray Sum Equals K, 
Two Sum IV - Input is a BST, Two Sum Less Than K
'''
