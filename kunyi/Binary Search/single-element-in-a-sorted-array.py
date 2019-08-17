class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        # binary search 
        result = None 
        for num in nums:
            if result == num:
                result = None 
            elif result is None:
                result = num 
                
        return result

    
###### binary search #######
class Solution:
    def singleNonDuplicate(self, xs):
        n = len(xs)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = int(lo + (hi-lo)/2)
            if mid and xs[mid-1] == xs[mid]:
                if mid-2 >= lo and (mid-lo-1) % 2 != 0:
                    hi = mid-2
                else:
                    lo = mid+1
            elif mid+1 < n and xs[mid+1] == xs[mid]:
                if mid+2 <= hi and (hi-mid-1) % 2 != 0:
                    lo = mid+2
                else:
                    hi = mid-1
            else:
                return xs[mid]
        raise ValueError
