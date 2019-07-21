"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # Nlog(k)
        import heapq
        result = []
        heap = []
        for i in range(len(intervals)):
            if len(intervals[i]) > 0:
                heapq.heappush(heap, (intervals[i][0].start, intervals[i][0], i, 0))
                
        while heap:
            interval_start, interval, row, ind = heapq.heappop(heap)
            self.push_back(result, interval)
            if ind + 1 < len(intervals[row]):
                heapq.heappush(heap, (intervals[row][ind+1].start, intervals[row][ind+1], row, ind + 1))
                
        return result 
        
    def push_back(self, result, interval):
        if len(result) == 0 or result[-1].end < interval.start:
            result.append(interval)
        else:
            result[-1].end = max(result[-1].end, interval.end)
            
        return
