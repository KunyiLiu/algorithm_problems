class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        count, max_length = 0, 0
        d = {0:0}
        for i, n in enumerate(nums, 1):
            if n == 0:
                count -= 1 
            else:
                count += 1 
            
            if count not in d:
                d[count] = i 
            else:
                max_length = max(max_length, i - d[count])
        return max_length
        

'''
Success
Details 
Runtime: 968 ms, faster than 87.25% of Python3 online submissions for Contiguous Array.
Memory Usage: 18.2 MB, less than 16.67% of Python3 online submissions for Contiguous Array.
Next challenges: Maximum Size Subarray Sum Equals k
'''
