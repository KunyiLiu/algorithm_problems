class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # not unique 
        # use hash table to record #elem on the list nums1 
        # loop through nums2, if counter > 0, append, and subtract the #elem from 1 
        import collections
        result = []
        counter = collections.Counter(nums1)
        for num in nums2:
            if counter[num] > 0:
                result.append(num)
                counter[num] -= 1 
                
        return result
