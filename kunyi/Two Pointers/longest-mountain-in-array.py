################### ENUM from mid/mountain peak    ######################
######## reference: longest-palindromic-substring.py ################
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        # enum from mid 
        n = len(A)
        if n < 3:
            return 0 
        self.longest = 0
        for mid in range(1, n-1):
            self.helper(A, mid-1, mid+1)
        
        # error: dont ignore the def of mountain
        return self.longest if self.longest >= 3 else 0
    
    def helper(self, A, left, right):
        # error 
        if A[left] >= A[left+1] or A[right] >= A[right-1]:
            return
        while left >= 0 and A[left] < A[left+1]:
            left -= 1 
        while right < len(A) and A[right] < A[right-1]:
            right += 1 
        local = (right - 1) - (left + 1) + 1
        self.longest = max(self.longest, local)



#####################  O(n) ############################
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0 
        
        longest = 0 
        start, end = 0, 0
        while start < n:
            if end + 1 < n and A[end] < A[end+1]:  # if start is a left-boundary
                #set end to the peak of this potential mountain
                while end + 1 < n and A[end] < A[end+1]: 
                    end += 1
                    
                if end + 1 < n and A[end] > A[end+1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end + 1 < n and A[end] > A[end+1]:
                        end += 1 
                    longest = max(longest, end - start + 1)
                    
            start = max(end, start + 1)
            end = start 
            
        return longest
