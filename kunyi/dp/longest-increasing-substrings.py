class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # O(n^2)
        # dp[] = [1] * len(nums), dp[i] - the length of LIS dp[0:(i+1)]
        if nums is None or len(nums) == 0:
            return 0 
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            tmp = dp[i]
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    tmp = dp[j] + 1 if dp[j] + 1 > tmp else tmp
            dp[i] = tmp

        return max(dp)
    
    
    class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # O(nlogn) - using binary search
        # minLast - record the min value of the last element of the subtring with len i
        # 有多个位置，以这些位置为结尾的LIS长度都为i， 则这些数字中最小的一个存在B[i]中
        if nums is None or len(nums) == 0:
            return 0
        import sys 
        min_int, max_int = - sys.maxsize - 1, sys.maxsize
        minLast = [max_int if i > 0 else min_int for i in range(len(nums)+1)]
        for i in range(len(nums)):
            # find the index of the first number in minLast >= nums[i]
            index = self.binary_search(minLast, nums[i])
            minLast[index] = nums[i]
            
        result = None    
        for i in range(1, len(nums) + 1):
            if minLast[i] == max_int:
                break 
            result = i
            
        return result 
        
        
    def binary_search(self, minLast, number):
        start, end = 0, len(minLast) - 1 
        while start + 1 < end: 
            mid = start + (end - start) // 2 
            if minLast[mid] > number:
                end = mid 
            else:
                start = mid
                
        if minLast[start] >= number:
            return start 
            
        return end 
