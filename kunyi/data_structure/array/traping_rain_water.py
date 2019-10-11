class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # two pointers
        # 4 2 3 start from the lower end
        result = 0
        l, r = 0, len(heights) - 1 
        while l < r:
            i = 1 
            if heights[l] < heights[r]:
                while heights[l] > heights[l+i]:
                    result += (heights[l] - heights[l+i])
                    i += 1 
                l = l + i
            else:
                while heights[r] > heights[r-i]:
                    result += (heights[r] - heights[r-i])
                    i += 1 
                r = r - i 
                
        return result
