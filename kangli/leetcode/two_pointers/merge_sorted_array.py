class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        k = m + n -1
        m -= 1
        n -= 1
        while m >=0 and n >=0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                k -= 1
                m -= 1 
            else:
                nums1[k] = nums2[n]
                n -= 1
                k -= 1 
        while n >=0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1


'''
Success
Details 
Runtime: 48 ms, faster than 35.79% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.9 MB, less than 5.02% of Python3 online submissions for Merge Sorted Array.
Next challenges: Interval List Intersections

Related Topics: Array, Two Pointers
Similar Questions: Merge Two Sorted Lists, Squares of a Sorted Array, Interval List Intersections
'''
