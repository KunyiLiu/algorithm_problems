class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # basically is calculating max(prefix_sum[i] - prefix_sum[j])
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])


        max_subarray_sum = nums[0]
        min_prefix_sum = prefix_sum[0]
        for i in range(1, n + 1):
            max_subarray_sum = max(max_subarray_sum, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

        return max_subarray_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane’s Algorithm, when the running sum is negative, reset it and 
        # start a fresh subarray from the next element
        # Time complexity: O(n), Space Complexity: O(1)
        n = len(nums)
        if n < 1:
            return 

        cur_sum, max_sum = 0, nums[0]
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            max_sum = max(max_sum, cur_sum)

        return max_sum

        
