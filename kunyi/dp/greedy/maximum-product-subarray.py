####### max // min #####
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # greedy - similar to best time to buy
        # min_subarray = min(..., current)
        # max_subarray = max(.., current // min_subarray if not 0)
        if nums is None or len(nums) == 0:
            return 
        
        min_subarray_positive, max_subarray_negative = 1, 1
        max_subarray, current = -99999, 1
        for i in range(len(nums)):
            current = current * nums[i] if current else nums[i]
            if current > 0 :
                max_subarray = max(max_subarray, current // min_subarray_positive)
                min_subarray_positive = min(min_subarray_positive, current)
            elif current < 0:
                max_subarray = max(max_subarray, current // max_subarray_negative)
                if max_subarray_negative > 0 or abs(max_subarray_negative) >= abs(current):
                    max_subarray_negative = current
            else:
                max_subarray = max(max_subarray, current)
                current = 1
                min_subarray_positive, max_subarray_negative = 1, 1
                
            
        return max_subarray 
        
 ####### record minVal and maxVal at the same time ######
