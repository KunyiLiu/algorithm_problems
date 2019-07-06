class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        n = len(nums)
        count, left, prod = 0, 0, 1

        for right, n in enumerate(nums):
            prod *= n
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count


'''
Success
Details
Runtime: 264 ms, faster than 96.38% of Python3 online submissions for Subarray Product Less Than K.
Memory Usage: 15.8 MB, less than 75.00% of Python3 online submissions for Subarray Product Less Than K.
Next challenges:
Maximum Product Subarray
Maximum Size Subarray Sum Equals k
Subarray Sum Equals K
Two Sum Less Than K

Related Topics: Array, Two Pointers
Similar Questions: Maximum Product Subarray, Maximum Size Subarray Sum Equals k, Subarray Sum Equals K
Two Sum Less Than K
Hint: For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j]
 is less than k. opt is an increasing function.
'''
