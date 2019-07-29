class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
        

'''
Success
Details 
Runtime: 72 ms, faster than 93.95% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 14.8 MB, less than 7.39% of Python3 online submissions for Kth Largest Element in an Array.
Next challenges: Wiggle Sort II, Top K Frequent Elements, Third Maximum Number, Kth Largest Element in a Stream

Related Topics: Divide and Conquer, Heap
Similar Questions: Medium, Top K Frequent Elements, Third Maximum Number, Kth Largest Element in a Stream, 
K Closest Points to Origin
'''
