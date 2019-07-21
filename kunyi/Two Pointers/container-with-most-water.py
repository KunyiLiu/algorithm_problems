class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # goal: get the max of (j-i)*min(ai, aj)
        # two pointers start, end = 0, n-1 
        # ai < aj, i += 1 
        # ai > aj, j -= 1 
        # (j-i) maximized, try to increase min(ai, aj)
        n = len(heights)
        start, end = 0, n - 1 
        result = 0
        while start < end: 
            result = max(result, (end - start) * min(heights[start], heights[end]))
            if heights[start] < heights[end]:
                start += 1 
            else:
                end -= 1 
                
        return result 
