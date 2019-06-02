class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # result from small to large is [max(pages), .., sum(pages)]
        # find the smallest result when its number_of_group == k 
        if pages is None or len(pages) == 0:
            return 0 
        # k <= len(pages)
        if k >= len(pages):
            return max(pages)
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2 
            # when result smaller, needs more people to copy
            if self.number_of_group(pages, mid) > k:
                start = mid 
            else:
                end = mid 
                
        if self.number_of_group(pages, start) == k:
            return start 
        return end 
            
    def number_of_group(self, pages, target):
        k = target
        number, i = 1, 0
        while i < len(pages):
            if pages[i] > k:
                number += 1 
                k = target
            else:
                k -= pages[i]
                i += 1 
                
        return number 
