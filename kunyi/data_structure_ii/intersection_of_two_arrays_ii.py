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
    
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # sort + two pointers 
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        p1, p2 = 0, 0 
        result = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1 
            elif nums1[p1] > nums2[p2]:
                p2 += 1 
            else:
                result.append(nums1[p1])
                p1 += 1 
                p2 += 1 
                
        return result 
