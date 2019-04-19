class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # dp [[2,3], [5,4], [6,4], [6,7]]
        # sort first, and then find the longest ascending substring
        
        """ 使用二分查找法来优化速度，我们首先要做的还是给信封排序，但是这次排序和上面有些不同，信封的宽度还是从小到大排，但是宽度相等时，我们让高度大的在前面。那么现在问题就简化了成了找高度数字中的LIS，完全就和之前那道Longest Increasing Subsequence一样了"""
        import sys 
        max_int, min_int = sys.maxsize, -sys.maxsize -1
        
        if envelopes is None or len(envelopes) == 0:
            return 0 
            
        def cmp_func(x, y):
            if x[0] == y[0]:
                return y[1] - x[1]
            return x[0] - y[0]
            
        # envelopes = sorted(envelopes, cmp=cmp_func)
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        heights = [i[1] for i in envelopes]
        # LIS dp[i] - the min val for the IS with length i
        dp = [max_int if i > 0 else min_int for i in range(len(envelopes) + 1)]
        for i in range(len(heights)):
            # find the first number in dp >= heights[i]
            ind = self.binary_search(dp, heights[i])
            dp[ind] = heights[i]
        

        for i in range(1, len(heights) + 1):
            if dp[i] == max_int:
                return i - 1
        
        return i
                 
                 
    def binary_search(self, dp, number):
        start, end = 0, len(dp) - 1 
        while start + 1 < end: 
            mid = start + (end - start) / 2 
            if dp[mid] < number:
                start = mid 
            else:
                end = mid 
        
        if dp[start] >= number:
            return start 
        return end 
