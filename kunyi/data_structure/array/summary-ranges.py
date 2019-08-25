class Solution:
    """
    @param nums:  a sorted integer array without duplicates
    @return: the summary of its ranges
    """
    def summaryRanges(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return []
            
        start, end = nums[0], nums[0]
        result = []
        for i, num in enumerate(nums[1:]):
            if end + 1 == num:
                end = num 
            else:
                result.append(str(start) if start == end else '{}->{}'.format(start, end))
                start, end = num, num 
        result.append(str(start) if start == end else '{}->{}'.format(start, end))     
        return result 
