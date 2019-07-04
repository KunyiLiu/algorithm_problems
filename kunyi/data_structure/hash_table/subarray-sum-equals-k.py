######### TLE, (i,j) does not matter this time############
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # sub_sum[i] - sub_sum[j] = k, j < i 
        # time O(n^2)
        subarray_sum = {}
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                subarray_sum[i] = nums[i]
            else:
                subarray_sum[i] = subarray_sum[i-1] + nums[i]
                
        for i in range(1, len(nums)):
            if subarray_sum[i] == k:
                ans += 1
            for j in range(i):
                if subarray_sum[i] - subarray_sum[j] == k:
                    ans += 1 
                    
        return ans
        
######### O(N) ###############
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # subarray_sum[sub_sum] = count, j < i 
        # compare and generate sub_sum at the same time
        # time O(N)
        subarray_sum = {0: 1}
        ans = 0
        curr_sum = 0 
        for num in nums:
            curr_sum += num
            subarray_sum[curr_sum] = subarray_sum.get(curr_sum, 0) + 1 
            if curr_sum - k in subarray_sum:
                ans += subarray_sum[curr_sum - k]
                    
        return ans
